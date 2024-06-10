# Generated by Django 3.1.7 on 2021-03-20 17:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yad', '0003_yad_quran_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='yad',
            name='reyad',
            field=models.ManyToManyField(blank=True, related_name='reyad', to=settings.AUTH_USER_MODEL, verbose_name='باز  نشر'),
        ),
    ]
