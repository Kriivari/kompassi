# encoding: utf-8

from core.helpers import person_required
from core.models import Event
from core.utils import get_code, initialize_form

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import ugettext_lazy as _

from ..helpers import enrollment_event_required
from ..models import Enrollment

@enrollment_event_required
@person_required
def enrollment_enroll_view(request, event):
    meta = event.enrollment_event_meta

    already_enrolled = Enrollment.objects.filter(
        event=event,
        person=request.user.person,
    ).exists()

    if already_enrolled:
        # TODO Display
        messages.error(request, _("You are already enrolled in this event."))
        return redirect('core_event_view', event.slug)

    mandatory_information_missing = not (
        request.user.person
    )

    EnrollmentForm = meta.form_class
    form = initialize_form(EnrollmentForm, request)

    if request.method == 'POST':
        # TODO Allow changing/cancelling enrollment as long as enrollment period is open

        if mandatory_information_missing:
            messages.error(request, _("Missing mandatory information."))
        elif not form.is_valid():
            messages.error(request, _("Please check the form."))
        else:
            enrollment = form.save(commit=False)
            enrollment.event = event
            enrollment.person = request.user.person
            enrollment.save()
            form.save_m2m()

            messages.success(request,
                _("Thank you for enrolling.")
            )
            return redirect('core_event_view', event.slug)

    vars = dict(
        already_enrolled=already_enrolled,
        event_slug = event,
        form=form,
        mandatory_information_missing=mandatory_information_missing,
    )

    return render(request, 'enrollment_enroll_view.jade', vars)
