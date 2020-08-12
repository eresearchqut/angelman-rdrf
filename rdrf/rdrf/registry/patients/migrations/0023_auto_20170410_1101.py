# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 11:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_patient_date_of_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='clinician',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Clinician'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(
                verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_migration',
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name='Date of migration'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
                verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ethnic_origin',
            field=models.CharField(
                blank=True,
                choices=[
                    ('New Zealand European',
                     'New Zealand European'),
                    ('Australian',
                     'Australian'),
                    ('Other Caucasian/European',
                     'Other Caucasian/European'),
                    ('Aboriginal',
                     'Aboriginal'),
                    ('Person from the Torres Strait Islands',
                     'Person from the Torres Strait Islands'),
                    ('Maori',
                     'Maori'),
                    ('NZ European / Maori',
                     'NZ European / Maori'),
                    ('Samoan',
                     'Samoan'),
                    ('Cook Islands Maori',
                     'Cook Islands Maori'),
                    ('Tongan',
                     'Tongan'),
                    ('Niuean',
                     'Niuean'),
                    ('Tokelauan',
                     'Tokelauan'),
                    ('Fijian',
                     'Fijian'),
                    ('Other Pacific Peoples',
                     'Other Pacific Peoples'),
                    ('Southeast Asian',
                     'Southeast Asian'),
                    ('Chinese',
                     'Chinese'),
                    ('Indian',
                     'Indian'),
                    ('Other Asian',
                     'Other Asian'),
                    ('Middle Eastern',
                     'Middle Eastern'),
                    ('Latin American',
                     'Latin American'),
                    ('Black African/African American',
                     'Black African/African American'),
                    ('Other Ethnicity',
                     'Other Ethnicity'),
                    ('Decline to Answer',
                     'Decline to Answer')],
                max_length=100,
                null=True,
                verbose_name='Ethnic origin'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_name',
            field=models.CharField(
                db_index=True,
                max_length=100,
                verbose_name='Family Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='given_names',
            field=models.CharField(
                db_index=True,
                max_length=100,
                verbose_name='Given Names'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_phone',
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name='Home phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='living_status',
            field=models.CharField(
                choices=[
                    ('Alive',
                     'Living'),
                    ('Deceased',
                     'Deceased')],
                default='Alive',
                max_length=80,
                verbose_name='Living status'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile_phone',
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name='Mobile phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin_email',
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
                verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin_family_name',
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name='Family name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin_given_names',
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name='Given names'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin_home_phone',
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name='Home phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin_mobile_phone',
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name='Mobile phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin_work_phone',
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name='Work phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rdrf_registry',
            field=models.ManyToManyField(
                related_name='patients',
                to='rdrf.Registry',
                verbose_name='Rdrf Registry'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(
                choices=[
                    ('1',
                     'Male'),
                    ('2',
                     'Female'),
                    ('3',
                     'Indeterminate')],
                max_length=1,
                verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='work_phone',
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name='Work phone'),
        ),
        migrations.AlterField(
            model_name='patientaddress',
            name='address_type',
            field=models.ForeignKey(
                default=1,
                on_delete=models.CASCADE,
                to='patients.AddressType',
                verbose_name='Address type'),
        ),
        migrations.AlterField(
            model_name='patientaddress',
            name='country',
            field=models.CharField(
                max_length=100,
                verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='patientaddress',
            name='postcode',
            field=models.CharField(
                max_length=50,
                verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='patientaddress',
            name='state',
            field=models.CharField(
                max_length=50,
                verbose_name='State'),
        ),
    ]
