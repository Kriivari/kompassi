# Generated by Django 2.1.4 on 2019-01-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frostbite2019', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='shirt_type',
            field=models.CharField(choices=[('NO_SHIRT', 'Ei paitaa'), ('STAFF', 'Staff'), ('DESURITY', 'Desurity'), ('DESUTV', 'DesuTV'), ('KUVAAJA', 'Kuvaaja'), ('VENDOR', 'Myynti'), ('TOOLATE', 'Myöhästyi paitatilauksesta')], default='TOOLATE', max_length=8, verbose_name='Paidan tyyppi'),
        ),
    ]
