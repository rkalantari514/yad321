from django.shortcuts import render

# Create your views here.
from mycity.models import State
from yad.models import Yad


def for_city_tab(request, *args, **kwargs):
    state= State.objects.order_by("name").all()
    stateno=[]
    for st in state:
        st_name=st.name
        st_yadbood=Yad.objects.filter(state=st).count()
        if st_yadbood > 0 :
            stateno.append((st_name,st_yadbood,st.id))
    # print(stateno)



    context = {
        # 'state': state,
        'stateno':stateno
    }
    return render(request, 'bycity/for_city_tab.html', context)


def states(request):
    state= State.objects.order_by("name").all()
    stateno=[]
    for st in state:
        st_name=st.name
        st_yadbood=Yad.objects.filter(state=st).count()
        print(st_name)
        print(st_yadbood)
        if st_yadbood > 0 :
            stateno.append((st_name,st_yadbood,st.id))
    context = {
        'stateno':stateno,
        'title':"یادبود های استان ها"
    }
    return render(request, 'bycity/states.html', context)