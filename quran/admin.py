from django.contrib import admin

# Register your models here.
from quran.models import Quran, Quran_set, Site_setting


class QuranAdmin(admin.ModelAdmin):
    list_display = ['page','is_read']
    list_editable = ['is_read']








    class Meta:
        model = Quran

class Quran_setAdmin(admin.ModelAdmin):
    list_display = ['__str__','total_count']

    class Meta:
        model = Quran_set




admin.site.register(Quran,QuranAdmin)
admin.site.register(Quran_set,Quran_setAdmin)
admin.site.register(Site_setting)
