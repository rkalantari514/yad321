from django.contrib import admin

# Register your models here.
from yad.models import Yad


class YadAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name','family','active','owner']
    # list_filter = ['active']
    list_editable = ['name','family','active','owner']
    search_fields = ['name','family']
    list_per_page = 20
    sortable_by = ['name','family','active']







    class Meta:
        model = Yad


admin.site.register(Yad,YadAdmin)
