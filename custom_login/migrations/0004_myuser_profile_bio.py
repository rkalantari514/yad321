# Generated by Django 3.1.7 on 2021-03-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_login', '0003_auto_20210322_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile_bio',
            field=models.TextField(blank=True, null=True, verbose_name='بیوگرافی'),
        ),
    ]
