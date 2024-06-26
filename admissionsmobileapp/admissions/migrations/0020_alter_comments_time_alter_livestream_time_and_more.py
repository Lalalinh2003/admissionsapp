# Generated by Django 5.0.1 on 2024-02-26 17:23

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0019_comments_user_questions_user_alter_comments_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 0, 23, 47, 592908)),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 0, 23, 47, 592908)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
