# Generated by Django 5.0.1 on 2024-02-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0012_rename_annouce_livestream_announce'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='beforeLive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questions',
            name='duringLive',
            field=models.BooleanField(default=False),
        ),
    ]
