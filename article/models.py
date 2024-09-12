from django.db import models

# Create your models here.
class Article(models.Model):
    title  = models.CharField(max_length=150,null=True,blank=True, verbose_name='موضوع')

    def __str__(self):
        return self.title