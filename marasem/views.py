from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from jalali_date import datetime2jalali

from custom_login.models import MyUser
from marasem.form import CreateMarasemForm
from marasem.models import Marasem
from mycity.models import City
from yad.models import Yad


@login_required(login_url='/register')
def CreateNewEvent(request,*args,**kwargs):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    yadId=kwargs['yadId']
    yadbood=Yad.objects.filter(id=yadId).first()
    owner = yadbood.owner



    create_form = CreateMarasemForm(request.POST or None
                                # initial={'first_name': user.first_name, 'last_name': user.last_name}
                                )

    context = {'create_form': create_form,
               'yad':yadbood,
               'title':"ایجاد مراسم"

               }

    if user!=owner:
        raise Http404('شما این دسترسی را ندارید')

    if user==owner:
        if create_form.is_valid():
            title = create_form.cleaned_data.get('title')
            address = create_form.cleaned_data.get('address')
            event_date= create_form.cleaned_data.get('event_date')
            finishtime= create_form.cleaned_data.get('finishtime')
            starttime= create_form.cleaned_data.get('starttime')
            state= create_form.cleaned_data.get('state')
            city= create_form.cleaned_data.get('city')


            Marasem.objects.create(
                title=title,
                state=state,
                city=city,
                address=address,
                event_date= event_date,
                finishtime=finishtime,
                starttime=starttime,
                yad=yadbood
            )
            return redirect(f"/yadbood/{yadId}")
    return render(request, 'event/create_event.html', context)


@login_required(login_url='/register')
def EditEvent(request,*args,**kwargs):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    yadId=kwargs['yadId']
    yadbood=Yad.objects.filter(id=yadId).first()
    owner = yadbood.owner
    eventID=kwargs['eventId']
    event_for_edit=Marasem.objects.filter(id=eventID).first()


    edit_event_form = CreateMarasemForm(request.POST or None,
                                initial={'title': event_for_edit.title,
                                         'state': event_for_edit.state,
                                         'city': event_for_edit.city,
                                         'address': event_for_edit.address,
                                         'event_date':event_for_edit.event_date,
                                         'starttime':event_for_edit.starttime,
                                         'finishtime':event_for_edit.finishtime,



                                         }
                                )
    context = {
        'edit_event_form': edit_event_form,
        'yad': yadbood,
        'title':"ویرایش مراسم"

    }

    if user==owner:
        if edit_event_form.is_valid():
            title = edit_event_form.cleaned_data.get('title')
            state = edit_event_form.cleaned_data.get('state')
            city = edit_event_form.cleaned_data.get('city')
            address = edit_event_form.cleaned_data.get('address')
            event_date= edit_event_form.cleaned_data.get('event_date')
            finishtime= edit_event_form.cleaned_data.get('finishtime')
            starttime= edit_event_form.cleaned_data.get('starttime')

            event_for_edit.title=title
            event_for_edit.state=state
            event_for_edit.city=city
            event_for_edit.address=address
            event_for_edit.event_date= event_date
            event_for_edit.finishtime=finishtime
            event_for_edit.starttime=starttime
            event_for_edit.save()
            return redirect(f"/yadbood/{yadId}")
    return render(request, 'event/edit_event.html', context)

@login_required(login_url='/register')
def DeleteEvent(request,*args,**kwargs):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    yadId=kwargs['yadId']
    yadbood=Yad.objects.filter(id=yadId).first()
    owner = yadbood.owner
    eventID=kwargs['eventId']
    event_for_delete=Marasem.objects.filter(id=eventID).first()



    if user==owner:
        if event_for_delete is not None:
            event_for_delete.delete()
            return redirect(f"/yadbood/{yadId}")

# AJAX
def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'event/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

