# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 22:04
from __future__ import unicode_literals

from django.db import migrations


def make_role_event_specific(apps, schema_editor):
    ProgrammeRole = apps.get_model('programme', 'programmerole')
    Role = apps.get_model('programme', 'role')
    PersonnelClass = apps.get_model('labour', 'personnelclass')

    PersonnelClass.objects.filter(name__icontains='ohjelma').update(app_label='programme')

    for programme_role in ProgrammeRole.objects.all():
        if programme_role.role.personnel_class is None:
            try:
                personnel_class = PersonnelClass.objects.get(
                    event=programme_role.programme.category.event,
                    name__in=[u'Ohjelma', u'Ohjelmanjärjestäjä']
                )
            except PersonnelClass.DoesNotExist:
                personnel_class = PersonnelClass(
                    event=programme_role.programme.category.event,
                    app_label='programme',
                    name=u'Ohjelmanjärjestäjä',
                    slug=u'ohjelma',
                    priority=40, # values of 0, 30 and 40 present; 40 most prevalent
                )
                personnel_class.save()

            old_role = programme_role.role

            programme_role.role, unused = Role.objects.get_or_create(
                personnel_class=personnel_class,
                title=old_role.title,
                defaults=dict(
                    require_contact_info=old_role.require_contact_info,
                    is_default=old_role.is_default,
                    is_public=old_role.is_public,
                )
            )

            programme_role.save()

    Role.objects.filter(personnel_class__isnull=True).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0016_auto_20160128_1805'),
        ('programme', '0019_auto_20160201_0003'),
    ]

    operations = [
        migrations.RunPython(make_role_event_specific, elidable=True),
    ]
