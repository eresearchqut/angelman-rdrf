# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-06 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0081_clinicaldata_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyrequest',
            name='survey_name',
            field=models.CharField(max_length=80),
        ),
    ]