from django.db import models


# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=40,verbose_name='نام استان')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')


    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=40,verbose_name='نام شهر')
    state = models.ForeignKey(State, on_delete=models.CASCADE,verbose_name='نام استان')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.name








#
# class City(models.Model):
#     city_name = models.CharField(max_length=150, verbose_name='نام شهر')
#     state_name = models.CharField(max_length=150,blank=True,null=True, verbose_name='نام استان')
#     is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
#
#
#     class Meta:
#         verbose_name = 'شهر'
#         verbose_name_plural = 'شهرها'
#
#     def __str__(self):
#         return "%s %s" % (self.city_name, self.state_name)
#




