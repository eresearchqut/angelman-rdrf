# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0042_add_context_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextformgroup',
            name='ordering',
            field=models.CharField(
                choices=[
                    ('C',
                     'Creation Time'),
                    ('N',
                     'Name')],
                default='C',
                max_length=1),
        ),
    ]