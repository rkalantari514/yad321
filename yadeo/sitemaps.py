from django.contrib.sitemaps import Sitemap

from yad.models import Yad


class YadSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Yad.objects.filter(active=True)