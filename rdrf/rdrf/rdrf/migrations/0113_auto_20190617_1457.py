# Generated by Django 2.1.7 on 2019-06-17 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0112_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification',
            name='context',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rdrf.RDRFContext'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verification',
            name='registry',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rdrf.Registry'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verification',
            name='patient_review_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rdrf.PatientReviewItem'),
            preserve_default=False,
        ),
    ]
