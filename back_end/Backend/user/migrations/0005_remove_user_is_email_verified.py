# Generated by Django 5.1.5 on 2025-01-21 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_is_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
    ]
