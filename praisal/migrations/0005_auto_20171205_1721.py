# Generated by Django 2.0 on 2017-12-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praisal', '0004_auto_20171205_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appraisement',
            old_name='parsed_content',
            new_name='parsed_items',
        ),
        migrations.AddField(
            model_name='appraisement',
            name='representative_kind',
            field=models.TextField(default='unknown'),
        ),
    ]