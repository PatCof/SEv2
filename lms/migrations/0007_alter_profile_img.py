# Generated by Django 4.2.7 on 2023-11-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='user.png', upload_to='images/'),
        ),
    ]
