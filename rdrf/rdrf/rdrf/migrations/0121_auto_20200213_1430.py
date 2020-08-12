# Generated by Django 2.1.12 on 2020-02-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0120_auto_20191217_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='customaction',
            name='scope',
            field=models.CharField(choices=[('U', 'Universal'), ('P', 'Patient')], default='U', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customaction',
            name='action_type',
            field=models.CharField(choices=[('PR', 'Patient Report'), ('SR', 'Patient Status Report')], max_length=2),
        ),
    ]
