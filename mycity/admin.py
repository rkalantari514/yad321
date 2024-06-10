from django.contrib import admin

# Register your models here.
# from city.models import City
#
#
from mycity.models import City, State


class CityAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name','state','is_active']

    class Meta:
        model = City

class StateAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name','is_active']

    class Meta:
        model = State


admin.site.register(State,StateAdmin)
admin.site.register(City,CityAdmin)
