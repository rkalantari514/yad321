from django.contrib import admin

from article.models import Article


# Register your models here.
class Article_Admin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Article




admin.site.register(Article,Article_Admin)