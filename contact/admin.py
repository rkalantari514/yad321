from django.contrib import admin

# Register your models here.
from .models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'text']
    list_per_page = 5
    sortable_by = ['is_read','subject', 'text','full_name']

admin.site.register(ContactUs, ContactAdmin)
