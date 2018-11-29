# encoding: utf-8

from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods

from core.utils import initialize_form
from mailings.models import Message
from mailings.forms import MessageForm

from ..helpers import labour_admin_required


@labour_admin_required
@require_http_methods(['GET', 'HEAD', 'POST'])
def labour_admin_mail_editor_view(request, vars, event, message_id=None):
    if message_id:
        message = get_object_or_404(Message, recipient__event=event, pk=int(message_id))
    else:
        message = None

    form = initialize_form(MessageForm, request, event=event, instance=message)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'delete':
            if message.is_sent:
                messages.error(request, 'Lähetettyä viestiä ei voi poistaa.')
            else:
                message.delete()
                messages.success(request, 'Viesti poistettiin.')

            return redirect('labour_admin_mail_view', event.slug)

        else:
            if form.is_valid():
                message = form.save(commit=False)

                if action == 'save-send':
                    message.save()
                    message.send()
                    messages.success(request, 'Viesti lähetettiin. Se lähetetään automaattisesti myös kaikille uusille vastaanottajille.')

                elif action == 'save-expire':
                    message.save()
                    message.expire()
                    messages.success(request, 'Viesti merkittiin vanhentuneeksi. Sitä ei lähetetä enää uusille vastaanottajille.')

                elif action == 'save-unexpire':
                    message.save()
                    message.unexpire()
                    messages.success(request, 'Viesti otettiin uudelleen käyttöön. Se lähetetään automaattisesti myös kaikille uusille vastaanottajille.')

                elif action == 'save-return':
                    message.save()
                    messages.success(request, 'Muutokset viestiin tallennettiin.')
                    return redirect('labour_admin_mail_view', event.slug)

                elif action == 'save-edit':
                    message.save()
                    messages.success(request, 'Muutokset viestiin tallennettiin.')

                else:
                    messages.error(request, 'Tuntematon toiminto.')

                return redirect('labour_admin_mail_editor_view', event.slug, message.pk)

            else:
                messages.error(request, 'Ole hyvä ja tarkasta lomake.')

    vars.update(
        message=message,
        form=form,
        sender="TODO",
    )

    return render(request, 'labour_admin_mail_editor_view.pug', vars)
