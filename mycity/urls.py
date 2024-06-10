from django.urls import path

from mycity.views import for_city_tab, states
from profile_page.views import profilepage

urlpatterns = [


    path('for_city_tab', for_city_tab, name="for_city_tab"),
    path('states', states, name="states"),

]