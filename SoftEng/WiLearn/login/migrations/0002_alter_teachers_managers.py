# Generated by Django 4.2.5 on 2023-10-05 14:43

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teachers',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]