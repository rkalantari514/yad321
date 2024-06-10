import os

from django.db import models

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    # final_name = f"{instance.id}{ext}"
    final_name = f"{instance.page}{ext}"
    return f"quran_pages/{final_name}"

def upload_sound_path(instance, filename):
    name, ext = get_filename_ext(filename)
    # final_name = f"{instance.id}{ext}"
    final_name = f"{instance.page}{ext}"
    return f"quran_sound/{final_name}"




class Quran(models.Model):
    page = models.IntegerField(default=1, verbose_name='صفحه')
    joz = models.IntegerField(default=1, verbose_name='جز')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر ')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده/خوانده نشده')
    read_count= models.IntegerField(default=0, verbose_name='دفعات خوانده شده')
    is_joz_readable= models.BooleanField(default=True, verbose_name='جزء قابل خواندن است')
    sound=models.FileField(null=True,blank=True,upload_to= upload_sound_path,verbose_name='صوت قرآن')


    class Meta:
        verbose_name = 'صفحه قرآن'
        verbose_name_plural = 'صفحات قرآن'

    # def __str__(self):
    #     return self.title


class Quran_set(models.Model):
    total_count = models.IntegerField( verbose_name='دفعات ختم کل')
    total_salavat = models.IntegerField(blank=True,null=True)
    total_fatehe = models.IntegerField(blank=True,null=True)
    total_yadbood = models.IntegerField(blank=True,null=True)



    class Meta:
        verbose_name = 'تنظیم ذکر'
        verbose_name_plural = 'تنظیمات ذکر و قرآن'






def upload_set_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"site/{final_name}"


class Site_setting(models.Model):
    logo = models.ImageField(upload_to=upload_set_image_path, null=True, blank=True, verbose_name='لوگو')
    about = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    site_name = models.CharField(max_length=150,null=True,blank=True, verbose_name='نام سایت')
    yad_image_default = models.ImageField(upload_to=upload_set_image_path, null=True, blank=True, verbose_name='تصویر ')
    conditions=models.TextField(verbose_name='قوانین ومقررات', null=True, blank=True)



