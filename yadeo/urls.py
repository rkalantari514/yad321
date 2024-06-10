"""yadeo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from yad.views import featured_render
from yadeo import settings
from yadeo.sitemaps import YadSitemap
from yadeo.views import home_page, header, Search, Capsule, Bottom, Sidebar, welcome, ShareActionSheet

sitemaps = {
    "yads": YadSitemap,
}


urlpatterns = [
    path('home', home_page),



    path('admin/', admin.site.urls),
    path('', include('custom_login.urls')),
    path('', include('yad.urls')),
    path('', include('quran.urls')),
    path('', include('profile_page.urls')),
    path('', include('marasem.urls')),
    path('', include('mycity.urls')),
    path('', include('contact.urls')),

    path('header', header, name="header"),
    path('footer', Search, name="Search"),
    path('Capsule', Capsule, name="Capsule"),
    path('Bottom', Bottom, name="Bottom"),
    path('Sidebar', Sidebar, name="Sidebar"),
    path('welcome', welcome, name="welcome"),
    path('ShareActionSheet', ShareActionSheet, name="ShareActionSheet"),
    path('featured_render', featured_render, name="featured_render"),
    
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),


]


# برای فایل های استاتیک
if settings.DEBUG:
    # add root static files

    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

