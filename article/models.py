import os
from django.db import models





def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_article_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    return f"article/{final_name}"






class Article(models.Model):
    title  = models.CharField(max_length=150,null=True,blank=True, verbose_name='موضوع')
    article_kinde  = models.CharField(max_length=150,null=True,blank=True, verbose_name='نوع')
    article_text = models.TextField(verbose_name='متن مقاله', null=True, blank=True)
    article_imge = models.ImageField(upload_to=upload_article_image_path, null=True, blank=True, verbose_name='تصویر مقاله')




    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title