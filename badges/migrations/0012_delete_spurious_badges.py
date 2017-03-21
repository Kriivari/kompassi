# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 20:11
from __future__ import unicode_literals

from django.db import migrations


def delete_spurious_badges(apps, schema_editor):
    Badge = apps.get_model('badges', 'badge')
    Badge.objects.filter(personnel_class__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0011_make_denormalized_fields_mandatory'),
    ]

    operations = [
        migrations.RunPython(delete_spurious_badges, elidable=True)
    ]
