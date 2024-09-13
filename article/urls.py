
from django.urls import path

from article.views import VArticle

urlpatterns = [
    path('article/<artId>', VArticle, name="newevent"),


]





