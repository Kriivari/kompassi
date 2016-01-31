# encoding: utf-8

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods

from core.utils import initialize_form
from labour.models import PersonnelClass

from ..forms import BadgeForm
from ..helpers import badges_admin_required


@badges_admin_required
@require_http_methods(['GET', 'HEAD', 'POST'])
def badges_admin_create_view(request, vars, event, personnel_class_slug=None):
    initial = dict()

    if personnel_class_slug is not None:
        personnel_class = get_object_or_404(PersonnelClass, event=event, slug=personnel_class_slug)
        initial.update(personnel_class=personnel_class)

    form = initialize_form(BadgeForm, request, prefix='badge_type', event=event, initial=initial)

    if request.method == 'POST':
        if form.is_valid():
            badge = form.save(commit=False)

            badge.is_first_name_visible = bool(badge.first_name)
            badge.is_surname_visible = bool(badge.surname)
            badge.is_nick_visible = bool(badge.nick)

            badge.created_by = request.user

            try:
                badge.full_clean()
            except ValidationError, e:
                messages.error(request, e.message)
            else:
                badge.save()

                messages.success(request, _(u'The badge has been added.'))
                return redirect('badges_admin_dashboard_view', event.slug)
        else:
            messages.error(request, _(u'Please check the form.'))

    vars.update(
        form=form,
    )

    return render(request, 'badges_admin_create_view.jade', vars)