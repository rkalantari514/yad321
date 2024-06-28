from django.urls import path
from yad.views import YadbodList, Yad_detail, add_salavat, add_100_salavat, Yad_detail_2, add_fatehe, reyad, CreateYad, \
    load_cities2, \
    EditYad, DeleteYad, yad_for_state, yad_for_city, SearchYadView, Yad_Total_Random, Yad_Total_Salavat, \
    Yad_Total_Fatehe, Yad_Total_Quran, Help,Send_eitaa,Reseteitaa

# path('yadbod' ,YadbodList.as_view()),




urlpatterns = [
    path('' ,YadbodList.as_view(),name="yadbodl"),
    path('help', Help, name="help"),
    path('sendeitaa', Send_eitaa, name="Sendeitaa"),
    path('reseteitaa', Reseteitaa, name="reseteitaa"),
    path('yadbood/<yadId>', Yad_detail_2, name="yadboodd"),
    path('yadbood/state/<stateId>/<page>', yad_for_state, name="yad_for_state"),
    path('yadbood/city/<cityId>/<page>', yad_for_city, name="yad_for_city"),
    
    path('yadbood/total_random/<page>', Yad_Total_Random, name="total_random"),
    path('yadbood/total_salavat/<page>', Yad_Total_Salavat, name="total_salavat"),
    path('yadbood/total_fatehe/<page>', Yad_Total_Fatehe, name="total_fatehe"),
    path('yadbood/total_quran/<page>', Yad_Total_Quran, name="total_quran"),

    path('search', SearchYadView.as_view()),




    #json
    path('yadbod/<yadId>', Yad_detail, name="yadbodd"),

    path('yadbod/<yadId>/salavat', add_salavat, name="salavat"),
    path('yadbod/<yadId>/100salavat', add_100_salavat, name="100salavat"),

    path('yadbod/<yadId>/fatehe', add_fatehe, name="fatehe"),
    path('yadbod/<yadId>/reyad', reyad, name="reyad"),


    path('create', CreateYad, name="create"),
    path('edit/<yadId>', EditYad, name="edit"),
    path('delete/<yadId>', DeleteYad, name="delete"),


    # Ajax
    path('ajax/load-cities2/', load_cities2, name='ajax_load_cities2'),  # AJAX

]

