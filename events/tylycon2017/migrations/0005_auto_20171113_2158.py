# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-13 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tylycon2017', '0004_auto_20161020_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='shift_type',
            field=models.CharField(choices=[('yksipitka', 'Yksi pitkä vuoro'), ('montalyhytta', 'Monta lyhyempää vuoroa'), ('kaikkikay', 'Kumpi tahansa käy')], help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?', max_length=15, verbose_name='Toivottu työvuoron pituus'),
        ),
        migrations.AlterField(
            model_name='signupextra',
            name='total_work',
            field=models.CharField(choices=[('4h', 'Minimi - 4 tuntia'), ('6h', '6 tuntia'), ('8h', '8 tuntia'), ('12h', '10–12 tuntia')], help_text='Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana?', max_length=15, verbose_name='Toivottu kokonaistyömäärä'),
        ),
    ]
