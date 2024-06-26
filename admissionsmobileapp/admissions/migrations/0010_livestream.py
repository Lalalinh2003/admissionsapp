# Generated by Django 5.0.1 on 2024-02-24 09:50

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0009_universityinfo_comments_time_information_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livestream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('annouce', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('questions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
