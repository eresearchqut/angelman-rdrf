# Generated by Django 2.1.15 on 2020-06-29 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0125_remove_custom_actions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientreview',
            name='context',
        ),
        migrations.RemoveField(
            model_name='patientreview',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='patientreview',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patientreview',
            name='review',
        ),
        migrations.RemoveField(
            model_name='patientreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patientreviewitem',
            name='patient_review',
        ),
        migrations.RemoveField(
            model_name='patientreviewitem',
            name='review_item',
        ),
        migrations.RemoveField(
            model_name='review',
            name='registry',
        ),
        migrations.RemoveField(
            model_name='reviewitem',
            name='form',
        ),
        migrations.RemoveField(
            model_name='reviewitem',
            name='review',
        ),
        migrations.RemoveField(
            model_name='reviewitem',
            name='section',
        ),
        migrations.DeleteModel(
            name='PatientReview',
        ),
        migrations.DeleteModel(
            name='PatientReviewItem',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='ReviewItem',
        ),
    ]