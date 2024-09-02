import os
import math

from django.db import models
from PIL import Image
from django.db.models import Q


# Create your models here.
from custom_login.models import MyUser
from mycity.models import State, City

from datetime import datetime
import datetime
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"yadbod/{final_name}"

class YadManager(models.Manager):

   def search(self, query):
        lookup = (
                Q(name__icontains=query) |
                Q(family__icontains=query)

         )
        yadi=Yad.objects.filter(lookup).distinct()
        return yadi




class Yad(models.Model):
    title = models.CharField(max_length=150, verbose_name='پیشوند', default='مرحوم')
    name = models.CharField(max_length=150, verbose_name='نام')
    family = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    master_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    # favio_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر اشتراک گذاری')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    salavat_count = models.IntegerField(default=0, verbose_name='تعداد صلوات')
    fatehe_count = models.IntegerField(default=0, verbose_name='تعداد فاتحه')
    quran_count = models.IntegerField(default=0, verbose_name='تعداد صفحات قرآن')
    owner = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='کاربر')
    reyad = models.ManyToManyField(MyUser, blank=True, related_name='reyad', verbose_name='باز  نشر')
    death_date= models.DateField(verbose_name='تاریخ فوت / شهادت' , null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, related_name='ostan', blank=True, null=True,
                              verbose_name='استان')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='shahr', blank=True, null=True,
                             verbose_name='شهر')
    is_featured=models.BooleanField(default=False, verbose_name='ویژه')

    objects=YadManager()



    class Meta:
        verbose_name = 'یادبود'
        verbose_name_plural = 'یادبودها'

    def __str__(self):
        # return self.title
        return "%s %s" % (self.name, self.family)

    def sad_salavat(self):
        s1=self.salavat_count/100
        s2= math.trunc(s1)
        return s2
    
    def get_absolute_url(self):
        return f"/yadbood/{self.id}"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.master_image.path)
        width, height = img.size  # Get dimensions
        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))
            width, height = img.size

            # check which one is smaller
            if height < width:
                # make square by cutting off equal amounts left and right
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))
                img.thumbnail((300, 300))
                img.save(self.master_image.path)

            elif width < height:
                # make square by cutting off bottom
                left = 0
                right = width
                top = 0
                bottom = width
                img = img.crop((left, top, right, bottom))
                img.thumbnail((300, 300))
                img.save(self.master_image.path)
            else:
                # already square
                img.thumbnail((300, 300))
                img.save(self.master_image.path)

        elif width > 300 and height == 300:
            left = (width - 300) / 2
            right = (width + 300) / 2
            top = 0
            bottom = 300
            img = img.crop((left, top, right, bottom))
            img.save(self.master_image.path)

        elif width > 300 and height < 300:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.save(self.master_image.path)

        elif width < 300 and height > 300:
            # most potential for disaster
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))
            img.save(self.master_image.path)

        elif width < 300 and height < 300:
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))
                img.save(self.master_image.path)
            elif width < height:
                height = width
                left = 0
                right = width
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))
                img.save(self.master_image.path)
            else:
                img.save(self.master_image.path)

        elif width == 300 and height > 300:
            # potential for disaster
            left = 0
            right = 300
            top = 0
            bottom = 300
            img = img.crop((left, top, right, bottom))
            img.save(self.master_image.path)

        elif width == 300 and height < 300:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.save(self.master_image.path)

        elif width < 300 and height == 300:
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))
            img.save(self.master_image.path)

        elif width and height == 300:
            img.save(self.master_image.path)

    def salg(self):
        m1 = self.death_date.month
        d1 = self.death_date.day
        now1 = datetime.datetime.now()
        y2 = datetime.datetime.now().year
        salgard = datetime.datetime(y2, m1, d1)
        if salgard < now1:
            salgard = datetime.datetime(y2 + 1, m1, d1)

        return salgard