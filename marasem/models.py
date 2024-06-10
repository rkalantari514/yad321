from django.db import models

# Create your models here.
from mycity.models import State, City
from yad.models import Yad


class Marasem(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان مراسم')
    address=models.TextField(verbose_name='آدرس', null=True, blank=True)
    event_date = models.DateField(verbose_name='تاریخ مراسم' , null=True, blank=True)
    starttime=models.TimeField(verbose_name='ساعت شروع مراسم' , null=True, blank=True)
    finishtime=models.TimeField(verbose_name='ساعت پایان مراسم' , null=True, blank=True)
    yad=models.ForeignKey(Yad,blank=True, null=True, on_delete=models.CASCADE ,verbose_name='یادبود')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    state = models.ForeignKey(State, on_delete=models.SET_NULL,related_name='state', blank=True, null=True, verbose_name='استان')
    city = models.ForeignKey(City, on_delete=models.SET_NULL,related_name='city', blank=True, null=True, verbose_name='شهر')


