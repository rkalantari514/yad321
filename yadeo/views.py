from django.shortcuts import render


def header(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Header.html', context)

def Search(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Search.html', context)


def Capsule(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Capsule.html', context)

def Bottom(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Bottom.html', context)

def Sidebar(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Sidebar.html', context)

def welcome(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/welcome.html', context)

def ShareActionSheet(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/ShareActionSheet.html', context)





def home_page(request):
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
    }
    return render(request, 'home_page.html', context)



def quran_page(request):
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
    }
    return render(request, 'quran/quran_page.html', context)