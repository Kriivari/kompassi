# encoding: utf-8

from __future__ import unicode_literals

from collections import defaultdict, namedtuple

from django.contrib import messages
from django.db.models import Count, Case, When
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from ..helpers import labour_admin_required


NO_SPECIAL_DIET_REPLIES = ['', '-', 'N/A', 'Ei ole', 'Ei ole.']


class DietRow(object):
    __slots__ = ('name', 'count')

    def __init__(self, name):
        self.name = name
        self.count = 0

    from core.utils import simple_object_repr as __repr__


class SpecialDiets(defaultdict):
    def __missing__(self, key):
        value = DietRow(key)
        self[key] = value
        return value


@labour_admin_required
def labour_admin_special_diets_view(request, vars, event):
    meta = event.labour_event_meta
    SignupExtra = meta.signup_extra_model
    SpecialDiet = SignupExtra.get_special_diet_model()
    special_diet_field = SignupExtra.get_special_diet_field()
    special_diet_other_field = SignupExtra.get_special_diet_other_field()

    if not any((special_diet_field, special_diet_other_field)):
        messages.error(request, _('This event does not record special diets.'))

    if special_diet_field:
        signup_extras_with_standard_special_diets = SignupExtra.objects.filter(
            is_active=True,
            special_diet__isnull=False
        )

        special_diets = SpecialDiets()

        for signup_extra in signup_extras_with_standard_special_diets:
            special_diets[signup_extra.formatted_special_diet].count += 1

        special_diets = special_diets.values()
        special_diets.sort(key=lambda sd: sd.name)
    else:
        special_diets = []

    if special_diet_other_field:
        # TODO assumes name special_diet_other
        signup_extras_with_other_special_diets = (
            SignupExtra.objects
                .filter(is_active=True)
                .exclude(special_diet_other__in=NO_SPECIAL_DIET_REPLIES)
        )
    else:
        signup_extras_with_other_special_diets = []

    vars.update(
        signup_extras_with_other_special_diets=signup_extras_with_other_special_diets,
        special_diet_field=special_diet_field,
        special_diet_other_field=special_diet_other_field,
        special_diets=special_diets,
    )

    return render(request, 'labour_admin_special_diets_view.jade', vars)
