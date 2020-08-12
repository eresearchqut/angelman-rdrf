# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-31 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0073_auto_20180830_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(max_length=80)),
                ('patient_token', models.CharField(max_length=80)),
                ('state', models.CharField(choices=[('requested', 'Requested'), ('completed', 'Completed')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('registry', models.ForeignKey(on_delete=models.CASCADE, to='rdrf.Registry')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('patient_token', models.CharField(max_length=80)),
                ('data', models.TextField()),
                ('registry', models.ForeignKey(on_delete=models.CASCADE, to='rdrf.Registry')),
            ],
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='precondition',
            field=models.ForeignKey(blank=True, null=True, 
                                    on_delete=models.CASCADE, to='rdrf.Precondition'),
        ),
    ]