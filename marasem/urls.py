
from django.urls import path

from marasem.views import CreateNewEvent, EditEvent, load_cities, DeleteEvent

urlpatterns = [
    path('newevent/<yadId>', CreateNewEvent, name="newevent"),
    path('editevent/<yadId>/<eventId>', EditEvent, name="editevent"),
    path('deleteevent/<yadId>/<eventId>', DeleteEvent, name="deleteevent"),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),  # AJAX

]





