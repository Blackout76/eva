# Generated by Django 2.0 on 2017-12-04 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praisal', '0002_auto_20171204_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appraisement',
            old_name='slug',
            new_name='code',
        ),
    ]
