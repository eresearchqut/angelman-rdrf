# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-13 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0085_cliniciansignuprequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliniciansignuprequest',
            name='speciality',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
