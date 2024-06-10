from django.shortcuts import render, redirect

# Create your views here.
from quran.models import Quran, Quran_set
from yad.models import Yad


def add_page(request,*args,**kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood=Yad.objects.filter(id=selected_yad_id).first()
    quran_page=Quran.objects.filter(is_read = False).first()
    quran_page.is_read=True
    yadbood.quran_count += 1
    quran_page.read_count += 1
    yadbood.save()
    quran_page.save()

    joz=quran_page.joz
    for pag in Quran.objects.filter(joz=joz):
        pag.is_joz_readable=False
        pag.save()

    # for new page
    quran_page=Quran.objects.filter(is_read = False).first()
    if quran_page is None:
        quran_set=Quran_set.objects.first()
        quran_set.total_count +=1
        quran_set.save()
        for page in Quran.objects.all():
            page.is_read = False
            page.is_joz_readable=True
            page.save()


    return redirect(f"/yadbood/{selected_yad_id}")


def add_joz(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()

    joz_page_first=Quran.objects.filter(is_joz_readable = True).first()
    print("---------1-----------")
    print(joz_page_first)
    if joz_page_first is not None:
        current_joz_no=joz_page_first.joz
        print('current_joz_no')
        print(current_joz_no)
        print("---------2-----------")
        pages=Quran.objects.filter(joz=current_joz_no)


        for pag in pages :
            print("---------3-----------")
            pag.is_read=True
            pag.is_joz_readable=False
            pag.read_count += 1
            pag.save()
            yadbood.quran_count += 1
            yadbood.save()



    # for new page
    quran_page = Quran.objects.filter(is_read=False).first()
    if quran_page is None:
        quran_set = Quran_set.objects.first()
        quran_set.total_count += 1
        quran_set.save()
        for page in Quran.objects.all():
            page.is_read = False
            page.is_joz_readable = True
            page.save()


    return redirect(f"/yadbood/{selected_yad_id}")





