from django.urls import path

from quran.views import add_page, add_joz

urlpatterns = [



    path('yadbod/<yadId>/page', add_page, name="page"),
    path('yadbod/<yadId>/joz', add_joz, name="joz"),



]

