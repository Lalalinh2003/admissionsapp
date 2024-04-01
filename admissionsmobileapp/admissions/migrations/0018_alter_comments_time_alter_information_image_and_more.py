# Generated by Django 5.0.1 on 2024-02-26 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0017_remove_information_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 23, 47, 37, 476666)),
        ),
        migrations.AlterField(
            model_name='information',
            name='image',
            field=models.ImageField(default=1, upload_to='information/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 23, 47, 37, 476666)),
        ),
    ]
