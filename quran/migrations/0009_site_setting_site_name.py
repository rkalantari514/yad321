# Generated by Django 3.1.7 on 2021-03-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0008_site_setting_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_setting',
            name='site_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='نام سایت'),
        ),
    ]
