# Generated by Django 2.0 on 2017-12-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField(max_length=8)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='parution date')),
            ],
        ),
    ]
