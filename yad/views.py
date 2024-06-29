#init 1
from datetime import datetime
import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

# Create your views here.
from django.views.generic import ListView, CreateView

from custom_login.models import MyUser
from marasem.models import Marasem
from mycity.models import City, State
from quran.models import Quran, Quran_set, Site_setting
from yad.forms import CreateYadForm
from yad.models import Yad
from jalali_date import datetime2jalali, date2jalali
from django.utils import timezone


# for eitaa
from os.path import isfile
import requests
from bs4 import BeautifulSoup
from time import sleep





def get_latest_messages(channel_id):
    r = requests.get(f"https://eitaa.com/{channel_id}")
    soup = BeautifulSoup(r.text, 'html.parser')
    pure_messages = soup.find_all('div', attrs={'class': 'etme_widget_message_bubble'})
    messages = []

    for message in pure_messages:
        message_text = message.find('div', class_='etme_widget_message_text').text.strip()
        views_element = message.find('span', class_='etme_widget_message_views')

        views = views_element.text.strip() if views_element else "Views not available"
        image_link = message.find('a', attrs={'class': 'etme_widget_message_photo_wrap'})

        image_url = ""
        if image_link:
            image_link = image_link['style']

            import re
            url_match = re.search(r"url\('([^']+)'\)", image_link)
            if url_match:
                image_url = url_match.group(1)
            else:
                print("Image URL not found")

        pure_time = message.find('span', class_='etme_widget_message_meta')
        iso_time = pure_time.a.time['datetime']
        message_number = pure_time.a['href'].split('/')[-1]

        messages.append({
            'image_link': f"https://eitaa.com/{image_url}" if image_url else None,
            'text': message_text,
            'views': views,
            'iso_time': iso_time,
            'message_number': int(message_number),
        })
        print('-------------')
        print(int(message_number))
    print(len(messages))
    print('*************')


    return messages

def send_file2(token, chat_id, caption, file, pin=False, date=None, view_to_delete=-1,
              disable_notification=False, reply_to_message_id=None):
    if not isfile(file):
        raise Exception(f"File `{file}` not found")

    r = requests.post(
        f"https://eitaayar.ir/api/{token}/sendFile",
        data={
            'chat_id': chat_id,
            'caption': caption,
            'pin': int(pin),
            'date': date,
            'viewCountForDelete': view_to_delete,
            'disable_notification': int(disable_notification),
            'reply_to_message_id': reply_to_message_id if reply_to_message_id != None else '',
        },
        files={
            'file': open(file, 'rb'),
        }
    )
    return r.json()





@login_required(login_url='/register')
def Send_eitaa(request, *args, **kwargs):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    if user.mobile != '09151006447':
        return redirect('/')
    yads=Yad.objects.filter(active=True)
    repo = []
    no1=0
    for yadbood in yads:
        repo.append('++++++++++++++++++++++++++++++++++++++++++++++++++')
        if yadbood.visit_count !=0 or no1 > 5:
            repo.append(f'yadbood.visit_count={yadbood.visit_count}')
            continue

        try:
            token = "bot19575:9926ae4d-395b-4aea-a412-467fbae01c65"
            cap1 = yadbood.title + " " + yadbood.name + " " + yadbood.family
            capdate=str(date2jalali(yadbood.death_date))
            year=capdate[0:4]
            month=capdate[5:7]
            day=capdate[8:]
            capdate=f'{year}/{month}/{day}'
            titledate='تاریخ فوت'
            if 'شهید' in yadbood.title:
                titledate = 'تاریخ شهادت'

            cap = f"""صفحه یادبود  {cap1}
www.yadeo.ir/yadbood/{yadbood.id}
{titledate}:{capdate}

از سایر یادبودهای این صفحه نیز بازدید فرمائید:
www.yadeo.ir/profile/{yadbood.owner.id}

یاداو|سامانه یادبود مجازی @yadeoir"""

            repo.append(cap)
            file = yadbood.master_image.file.name
            repo.append(file)

            repo.append(send_file2(token, "yadeoir", cap, file))
            repo.append('send')
            print('send')
            sleep(15)
            messageses = get_latest_messages('yadeoir')
            total = len(messageses) - 1
            last = messageses[int(total)]
            n = last.get('message_number')
            print(n)
            repo.append(f'number: {n}')
            yadbood.visit_count = n
            yadbood.save()
            no1+=1
        except:
            repo.append('ارسال نشد')

    context = {
        'repo': repo
    }

    return render(request,'yadbod/sendreport.html',context)


@login_required(login_url='/register')
def Reseteitaa(request):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    if user.mobile != '09151006447':
        return redirect('/')
    yads = Yad.objects.all()
    for y in yads:
        y.visit_count=0
        y.save()
    return redirect('/')



@login_required(login_url='/register')
def Delete2(request):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    if user.mobile != '09151006447':
        return redirect('/')
    yads = Yad.objects.all()
    for y in yads:
        vc=y.visit_count
        if vc ==0:
            continue
        if Yad.objects.filter(visit_count=vc).all().count() > 1:
            for yy in Yad.objects.filter(visit_count=vc).all():
                yy.visit_count = 0
                yy.save()


    return redirect('/')






def Help(request):

    context={   }
    return render(request,'yadbod/help.html',context)



class YadbodList(ListView):
    # paginate_by = 9

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(YadbodList, self).get_context_data(*args, **kwargs)
        quran_page = Quran.objects.filter(is_read=False).first()
        quran_set = Quran_set.objects.first()
        # quran_page_page = quran_page.page

        quran_page_page1 = 0
        for pag in Quran.objects.all():
            if pag.is_read:
                quran_page_page1 += 1
        quran_page_page100 = quran_page_page1 / 603

        state=State.objects.all()




        context['quran_set'] = quran_set
        context['quran_page'] = quran_page
        context['quran_page_page1'] = quran_page_page1
        context['quran_page_page100'] = quran_page_page100
        context['state'] = state,
        context['title'] = "سامانه یادبود مجازی"

        site_setting = Site_setting.objects.first()

        context['site_setting'] = site_setting





        return context

    def get_queryset(self):
        return Yad.objects.order_by('-id').filter(active=True)[:12]

    template_name = 'yadbod/yadbod_list.html'


# for salavat count
def Yad_detail(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()
    if yadbood is None:
        raise Http404('یادبود مورد نظر یافت نشد')

    quran_page = Quran.objects.filter(is_read=False).first()
    if quran_page is None:
        raise Http404('صفحه مورد نظر یافت نشد')

    quran_set = Quran_set.objects.first()
    if quran_set is None:
        raise Http404('کل قرآن  یافت نشد')

    user = request.user
    if user in yadbood.reyad.all():
        icon = "reyad-btn icon-box bg-success"
        is_reyad = True
    else:
        icon = "reyad-btn icon-box"
        is_reyad = False

    #sadjdeh
    sadjdeh = "alert alert-info mb-1 ju invisible"
    text1 = ""
    if quran_page.page == 416 or quran_page.page == 480 or quran_page.page == 597 or quran_page.page == 528:
        sadjdeh = "alert alert-info mb-1 ju"
        text1 = "این صفحه سجده واجب دارد!"


    return JsonResponse({
        'salavat_count': yadbood.salavat_count,
        'fatehe_count': yadbood.fatehe_count,
        'page': quran_page.page,
        'total_count': quran_set.total_count,
        'image': quran_page.image.url,
        'sound': quran_page.sound.url,
        'icon': icon,
        'is_reyad': is_reyad,
        'sadjdeh':sadjdeh,
        'text1':text1,
        'quran_count':yadbood.quran_count

    })


def Yad_detail_2(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()

    if yadbood is None:
        raise Http404('یادبود مورد نظر یافت نشد')
    # yadbood.visit_count += 1
    yadbood.save()
    owner = yadbood.owner.profile_name

    quran_page = Quran.objects.filter(is_read=False).first()

    quran_set = Quran_set.objects.first()

    user = request.user
    if user in yadbood.reyad.all():
        icon = "reyad-btn icon-box bg-success"
        is_reyad = True
    else:
        icon = "reyad-btn icon-box"
        is_reyad = False

    reyad_permision = request.user != yadbood.owner
    event_permision = False
    try:
        event_permision = request.user == yadbood.owner or user.mobile == '09151006447'
    except:
        pass
    title = f"یادبود مجازی {yadbood.title} {yadbood.name} {yadbood.family}"

    marasem = Marasem.objects.filter(yad=yadbood)

    for mar in marasem:
        now = timezone.now().date()
        if mar.event_date < now or mar.event_date is None:
            mar.active = False
            mar.save()

    marasem = Marasem.objects.order_by('event_date').filter(yad=yadbood, active=True)

    if not marasem is None:
        dates = []
        for mar in marasem:
            test = mar.event_date
            jalali = datetime2jalali(test).strftime('%Y/%m/%d')
            dates.append(jalali)

    joz_available = False
    current_joz_no = 0
    joz_page_first = Quran.objects.filter(is_joz_readable=True).first()
    if joz_page_first is not None:
        current_joz_no = joz_page_first.joz
        joz_available = True

    city_id=1
    state_id=1
    site_setting = Site_setting.objects.first()
    if yadbood.master_image is None:
        yadbood.master_image = site_setting.yad_image_default

    state=yadbood.state
    this_state=State.objects.filter(name=state).first()
    if this_state is not None:
        state_id=this_state.id

    city = yadbood.city
    this_city = City.objects.filter(name=city).first()
    if this_city is not None:
        city_id = this_city.id

    smsandroid=f"sms:?body=سلام لطفا از صفحه یادبود مجازی  {yadbood.title} {yadbood.name} {yadbood.family}  دیدن فرمایید.www.yadeo.ir/yadbood/{selected_yad_id}"
    smsforios=f"sms:&body=سلام لطفا از صفحه یادبود مجازی  {yadbood.title} {yadbood.name} {yadbood.family}  دیدن فرمایید.www.yadeo.ir/yadbood/{selected_yad_id}"
    telegram=f"tg://msg?text=http://yadeo.ir/yadbood/{ yadbood.id }"
    whatsapp=f"whatsapp://send?text=http://yadeo.ir/yadbood/{ yadbood.id }"
    eitaa=f"https://eitaa.com/share/url?url=http://yadeo.ir/yadbood/{ yadbood.id }"
    bale=f"bale://share?text=http://yadeo.ir/yadbood/{ yadbood.id }"
    sorosh=f"soroush://share?text=http://yadeo.ir/yadbood/{ yadbood.id }"

    have_sond= True
    if quran_page.sound is None:
        have_sond=False


    print("quran_page.sound.url")
    print(quran_page.sound)
    print(have_sond)


    #sadjdeh
    sadjdeh="alert alert-info mb-1 ju invisible"
    text1=""
    sad=False
    if quran_page.page == 416 or quran_page.page== 480 or quran_page.page == 597 or quran_page.page ==528:
        sadjdeh="alert alert-info mb-1 ju"
        text1="این صفحه سجده واجب دارد!"
        sad=True
    y1=yadbood.death_date.year
    m1=yadbood.death_date.month
    d1=yadbood.death_date.day

    now1=datetime.datetime.now()
    y2=datetime.datetime.now().year
    salgard=datetime.datetime(y2, m1, d1)
    if salgard < now1:
        salgard = datetime.datetime(y2+1, m1, d1)
    # s100=yadbood.salavat_count/100
    # sal100=math.trunc(s100)
    context = {
        'title': title,
        'yad': yadbood,
        # 'sal100':sal100,
        'quran_page': quran_page,
        'quran_set': quran_set,
        'icon': icon,
        'is_reyad': is_reyad,
        'reyad_permision': reyad_permision,
        'marasem': marasem,
        'event_permision': event_permision,
        'dates': dates,
        'current_joz_no': current_joz_no,
        'is_joz_available': joz_available,
        'state_id':state_id,
        'city_id':city_id,
        'smsandroid':smsandroid,
        'smsforios':smsforios,
        'telegram':telegram,
        'whatsapp':whatsapp,
        'eitaa':eitaa,
        'bale':bale,
        'sorosh':sorosh,
        'have_sound':have_sond,
        'sadjdeh':sadjdeh,
        'text1':text1,
        'sad':sad,
        'salgard':salgard,
        'now1':now1,

    }

    return render(request, 'yadbod/yadbod_detail.html', context)


def add_salavat(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()

    yadbood.salavat_count += 1
    yadbood.save()

    quran_setting = Quran_set.objects.first()
    quran_setting.total_salavat += 1
    quran_setting.save()

    return redirect(f"/yadbod/{selected_yad_id}")


def add_100_salavat(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()

    yadbood.salavat_count += 100
    yadbood.save()

    quran_setting = Quran_set.objects.first()
    quran_setting.total_salavat += 100
    quran_setting.save()

    return redirect(f"/yadbod/{selected_yad_id}")





def add_fatehe(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()
    yadbood.fatehe_count += 1
    yadbood.save()

    quran_setting = Quran_set.objects.first()
    quran_setting.total_fatehe += 1
    quran_setting.save()

    return redirect(f"/yadbod/{selected_yad_id}")


@login_required(login_url='/register')
def reyad(request, *args, **kwargs):
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()

    owner = yadbood.owner
    user = request.user
    if owner is not user:
        if user in yadbood.reyad.all():
            yadbood.reyad.remove(user)
        else:
            yadbood.reyad.add(user)
    return redirect("/")


@login_required(login_url='/register')
def CreateYad(request):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    site_setting = Site_setting.objects.first()
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    create_form = CreateYadForm(request.POST or None, request.FILES
                                # initial={'first_name': user.first_name, 'last_name': user.last_name}
                                )
    context = {
        'create_form': create_form,
        'title': "ایجاد یادبود جدید"
    }

    if create_form.is_valid():
        title = create_form.cleaned_data.get('title')
        name = create_form.cleaned_data.get('name')
        family = create_form.cleaned_data.get('family')
        description = create_form.cleaned_data.get('description')
        death_date = create_form.cleaned_data.get('death_date')
        state = create_form.cleaned_data.get('state')
        city = create_form.cleaned_data.get('city')
        image = create_form.cleaned_data.get('image')

        site_setting = Site_setting.objects.first()

        quran_set=Quran_set.objects.first()
        quran_set.total_yadbood +=1
        quran_set.save()


        if image is None:
            image = site_setting.yad_image_default

        Yad.objects.create(
            owner=user,
            title=title,
            name=name,
            family=family,
            master_image=image,
            description=description,
            death_date=death_date,
            state=state,
            city=city

        )

        context["create_form"] = CreateYadForm()
        return redirect('yadbodl')

    return render(request, 'yadbod/create.html', context)


@login_required(login_url='/register')
def EditYad(request, *args, **kwargs):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    selected_yad_id = kwargs['yadId']
    yadbood = Yad.objects.filter(id=selected_yad_id).first()
    if yadbood is None:
        raise Http404('یادبود مورد نظر یافت نشد')
    owner = yadbood.owner

    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    adm=True


    try:
        if user.mobile == '09151006447':
            adm=False
    except:
        pass

    if user != owner and adm:
        raise Http404('شما این دسترسی را ندارید')



    # print(yadbood.title)

    edit_form = CreateYadForm(request.POST or None, request.FILES or None,
                                  initial = {
        'title': yadbood.title,
        'name': yadbood.name,
        'family': yadbood.family,
        'description': yadbood.description,
        'death_date': yadbood.death_date,
        'state': yadbood.state,
        'city': yadbood.city,
    }
    )


    context = {
        'edit_form': edit_form,
        'yadbood':yadbood,
        'title':"ویرایش یادبود"
    }

    if edit_form.is_valid():
        yadbood.title = edit_form.cleaned_data.get('title')
        yadbood.name = edit_form.cleaned_data.get('name')
        yadbood.family = edit_form.cleaned_data.get('family')
        yadbood.description = edit_form.cleaned_data.get('description')
        yadbood.death_date = edit_form.cleaned_data.get('death_date')
        yadbood.state = edit_form.cleaned_data.get('state')
        yadbood.city = edit_form.cleaned_data.get('city')
        if edit_form.cleaned_data.get('image') is not None:
            yadbood.master_image = edit_form.cleaned_data.get('image')


        yadbood.save()



        context["edit_form"] = CreateYadForm()
        return redirect(f'/yadbood/{selected_yad_id}')

    return render(request, 'yadbod/edit.html', context)


@login_required(login_url='/register')
def DeleteYad(request, *args, **kwargs):
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)

    selected_yad_id = kwargs['yadId']
    yadbood_for_delete = Yad.objects.filter(id=selected_yad_id).first()
    if yadbood_for_delete is None:
        raise Http404('یادبود مورد نظر یافت نشد')
    owner = yadbood_for_delete.owner


    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    adm = True
    try:
        if user.mobile == '09151006447':
            adm = False
    except:
        pass

    if user != owner and adm:
        raise Http404('شما این دسترسی را ندارید')

    if user == owner:
        if yadbood_for_delete is not None:
                yadbood_for_delete.delete()
                quran_set = Quran_set.objects.first()
                quran_set.total_yadbood -= 1
                quran_set.save()
                return redirect('yadbodl')



def yad_for_state(reqest,*args,**kwargs):
    stateId= kwargs['stateId']
    state=State.objects.filter(id=stateId).first()
    yadbood=Yad.objects.filter(state=state)

    paginator = Paginator(yadbood, 12)
    page_number = kwargs['page']
    page_obj = paginator.get_page(page_number)

    len1 = len(paginator.page_range)
    stpage = 0
    finpage = 5
    if len1 > 5:
        stpage = int(page_number) - 3
        finpage = int(page_number) + 3

    cities=City.objects.order_by('name').filter(state=state)

    cityno = []
    for ci in cities:
        ci_name = ci.name
        ci_yadbood = Yad.objects.filter(city=ci).count()
        if ci_yadbood > 0:
            cityno.append((ci_name, ci_yadbood,ci.id))

    tit=f'شهرهای استان {state.name}'
    context={
        'yadbood':yadbood,
        'state': state.name,
        'cityno':cityno,
        'page_obj': page_obj,
        'paginator': paginator,
        'stpage': stpage,
        'finpage': finpage,
        'title': tit

    }

    return render(reqest,'yadbod/yad_for_state.html',context)



def yad_for_city(reqest,*args,**kwargs):
    cityId= kwargs['cityId']
    city=City.objects.filter(id=cityId).first()
    yadbood=Yad.objects.filter(city=city)

    paginator = Paginator(yadbood, 12)
    page_number = kwargs['page']
    page_obj = paginator.get_page(page_number)

    len1= len(paginator.page_range)
    stpage = 0
    finpage = 5
    if len1 > 5:
        stpage=int(page_number)-3
        finpage=int(page_number)+3
    context={
        'yadbood':yadbood,
        'page_obj':page_obj,
        'city': city.name,
        'cityid':cityId,
        'paginator':paginator,
        'stpage':stpage,
        'finpage':finpage,

    }

    return render(reqest,'yadbod/yad_for_city.html',context)

def featured_render(request):
    yadbood=Yad.objects.filter(is_featured = True)[:12]

    context={
        'yadbood':yadbood
    }

    return render(request,'yadbod/featured.html',context)


class SearchYadView(ListView):
    template_name = 'yadbod/search_result.html'

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Yad.objects.search(query)
        return Yad.objects.all()




# AJAX
def load_cities2(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'yadbod/city_dropdown_list_options.html', {'cities': cities})
    
def Yad_Total_Random(request,*args,**kwargs):
    yadbood = Yad.objects.order_by('id').all()

    paginator = Paginator(yadbood, 12)
    page_number = kwargs['page']
    page_obj = paginator.get_page(page_number)

    len1= len(paginator.page_range)
    stpage = 0
    finpage = 5
    if len1 > 5:
        stpage=int(page_number)-3
        finpage=int(page_number)+3

    dates = []
    for yad in yadbood:
        if not yad.death_date is None:
            test = yad.death_date
            jalali = datetime2jalali(test).strftime('%Y/%m/%d')
            dates.append(jalali)
   

    context={
        'yadbood':yadbood,
        'page_obj':page_obj,
        'paginator':paginator,
        'stpage':stpage,
        'finpage':finpage,
        'dates':dates,
    }

    return render(request,'yadbod/total_random.html',context)    
    
    
def Yad_Total_Salavat(request,*args,**kwargs):
    yadbood = Yad.objects.order_by('-salavat_count').all()
    paginator = Paginator(yadbood, 12)
    page_number = kwargs['page']
    page_obj = paginator.get_page(page_number)
    len1= len(paginator.page_range)
    stpage = 0
    finpage = 5
    if len1 > 5:
        stpage=int(page_number)-3
        finpage=int(page_number)+3

    context={
        'yadbood':yadbood,
        'page_obj':page_obj,
        'paginator':paginator,
        'stpage':stpage,
        'finpage':finpage,
    }
    return render(request,'yadbod/total_salavat.html',context)

def Yad_Total_Fatehe(request,*args,**kwargs):
    yadbood = Yad.objects.order_by('-fatehe_count').all()
    paginator = Paginator(yadbood, 12)
    page_number = kwargs['page']
    page_obj = paginator.get_page(page_number)
    len1= len(paginator.page_range)
    stpage = 0
    finpage = 5
    if len1 > 5:
        stpage=int(page_number)-3
        finpage=int(page_number)+3

    context={
        'yadbood':yadbood,
        'page_obj':page_obj,
        'paginator':paginator,
        'stpage':stpage,
        'finpage':finpage,
    }
    return render(request,'yadbod/total_fatehe.html',context)

def Yad_Total_Quran(request,*args,**kwargs):
    yadbood = Yad.objects.order_by('-quran_count').all()
    paginator = Paginator(yadbood, 12)
    page_number = kwargs['page']
    page_obj = paginator.get_page(page_number)
    len1= len(paginator.page_range)
    stpage = 0
    finpage = 5
    if len1 > 5:
        stpage=int(page_number)-3
        finpage=int(page_number)+3

    context={
        'yadbood':yadbood,
        'page_obj':page_obj,
        'paginator':paginator,
        'stpage':stpage,
        'finpage':finpage,
    }
    return render(request,'yadbod/total_quran.html',context)    
    
