# Generated by Django 3.1.7 on 2021-03-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yad', '0004_yad_reyad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yad',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]
