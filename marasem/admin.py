from django.contrib import admin

# Register your models here.
from marasem.models import Marasem
from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


class MarasemAdmin(admin.ModelAdmin):
    list_display = ['id','title','event_date','yad','active']
    class Meta:
        model = Marasem


admin.site.register(Marasem,MarasemAdmin)




