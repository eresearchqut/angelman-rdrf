# Generated by Django 2.1.5 on 2019-03-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0101_reviewitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewitem',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
