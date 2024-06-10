# Generated by Django 3.1.7 on 2021-03-22 14:26

import custom_login.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_login', '0002_auto_20210311_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=custom_login.models.upload_image_path, verbose_name='تصویر پروفایل'),
        ),
    ]
