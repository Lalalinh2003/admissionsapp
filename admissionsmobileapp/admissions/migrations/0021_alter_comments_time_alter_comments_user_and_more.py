# Generated by Django 5.0.1 on 2024-02-26 17:26

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0020_alter_comments_time_alter_livestream_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 0, 25, 59, 832006)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 0, 25, 59, 832006)),
        ),
    ]
