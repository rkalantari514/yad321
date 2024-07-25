import datetime
from datetime import datetime, timedelta

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

from quran.models import Site_setting
from .forms import RegisterForm, VerifyForm
from .models import MyUser
from . import helper
from django.contrib import messages


def register_view(request):
    regisrerForm = RegisterForm(request.POST or None)
    site_setting = Site_setting.objects.first()

    context = {
        'register_form': regisrerForm,
        'site_setting': site_setting
    }
    if regisrerForm.is_valid():
        yourmobile = regisrerForm.cleaned_data.get('mobile')
        user1 = MyUser.objects.filter(mobile=yourmobile).first()

        if user1 is None:
            print('user is none')
            MyUser.objects.create_user(mobile=yourmobile, password=None)
            user1 = MyUser.objects.filter(mobile=yourmobile).first()
            user1.profile_name=f"کاربر {user1.id}"
            # print(f"new user{user1}")
        else:
            now = datetime.now()
            otp_time = user1.otp_create_time
            dif_time = now - otp_time
            if dif_time.seconds < 2592000:
                return redirect(f'/verify/{yourmobile}')

        # send otp
        if user1.is_block:
            return redirect("/")
        if not user1.is_block:
            otp = helper.get_random_otp()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            helper.send_otp(yourmobile, otp)
            # helper.send_otp_soap(mobile, otp)
            # save otp
            print(otp)
            user1.otp = otp
            user1.save()
            return redirect(f'/verify/{yourmobile}')

        context = {
            'register_form': regisrerForm,
            'title': "ثبت نام",
            'site_setting': site_setting
        }

    return render(request, 'register.html', context)


# def register_view(request):
#     form = forms.RegisterForm
#     if request.method == "POST" :
#         try:
#             if "mobile" in request.POST:
#                 mobile = request.POST.get('mobile')
#                 user = MyUser.objects.get(mobile=mobile)
#                 # send otp
#                 otp = helper.get_random_otp()
#                 helper.send_otp(mobile, otp)
#                 # helper.send_otp_soap(mobile, otp)
#                 # save otp
#                 print(otp)
#                 user.otp = otp
#                 user.save()
#                 request.session['user_mobile'] = user.mobile
#                 return HttpResponseRedirect(reverse('verify'))
#
#         except MyUser.DoesNotExist:
#             form = forms.RegisterForm(request.POST)
#             if form.is_valid():
#                 # by me
#                 # mobile = request.POST.get('mobile')
#                 user = form.save(commit=False)
#                 # send otp
#                 otp = helper.get_random_otp()
#                 helper.send_otp(mobile, otp)
#                 # helper.send_otp_soap(mobile, otp)
#                 # save otp
#                 print(otp)
#                 user.otp = otp
#                 user.is_active = False
#                 user.save()
#                 request.session['user_mobile'] = user.mobile
#                 return HttpResponseRedirect(reverse('verify'))
#
#     context={
#         'form': form,
#         'title':'ورود / ثبت نام'
#     }
#     return render(request, 'register.html', context)


def verify(request, *args, **kwargs):
    yormobile = kwargs['mobile']
    print(yormobile)
    user = MyUser.objects.filter(mobile=yormobile).first()
    print(user)
    otp = user.otp
    print(otp)
    context = {}
    otp_create_time = user.otp_create_time
    print('otp_create_time')
    print(otp_create_time)
    if not helper.check_otp_expiration(user.mobile):
        context['message2']: "thi is finish"
        return redirect('register')

    now = datetime.now()
    otp_time = user.otp_create_time
    exp_otp_tim = str(otp_time + timedelta(seconds=2592000))
    resend_count = str(otp_time + timedelta(seconds=120))

    print('resend_count')
    print(resend_count)
    print(now)

    verifyForm = VerifyForm(request.POST or None, request.FILES or None)
    context = {
        'verify_form': verifyForm,
        'title': "تایید",
        'diff_time': exp_otp_tim,
        'yormobile': yormobile,
        'resend_count': resend_count
    }

    if verifyForm.is_valid():
        yuorotp = verifyForm.cleaned_data.get('yourotp')
        print(otp)
        print(yuorotp)
        if yuorotp == otp:
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(f'/profile/{user.id}')
        else:
            context = {
                'verify_form': verifyForm,
                'message': "کد وارد شده نامعتبر است",
                'diff_time': exp_otp_tim,
                'yormobile': yormobile,
                'resend_count': resend_count
            }

    return render(request, 'verify.html', context)

    # try:
    #     mobile = request.session.get('user_mobile')
    #     user = MyUser.objects.get(mobile = mobile)
    #
    #     if request.method == "POST":
    #
    #         # check otp expiration
    #         if not helper.check_otp_expiration(user.mobile):
    #             messages.error(request, "OTP is expired, please try again.")
    #             return HttpResponseRedirect(reverse('register_view'))
    #
    #         if user.otp != int(request.POST.get('otp')):
    #             messages.error(request, "OTP is incorrect.")
    #             return HttpResponseRedirect(reverse('verify'))
    #
    #         user.is_active = True
    #         user.save()
    #         login(request, user)
    #         return HttpResponseRedirect(reverse('dashboard'))
    #     context={
    #         'mobile': mobile,
    #         'title':'ثبت نام'
    #     }
    #     return render(request, 'verify.html', context)
    #     # return render(request, 'verify.html', {'mobile': mobile})
    #
    # except MyUser.DoesNotExist:
    #     messages.error(request, "Error accorded, try again.")
    #     return HttpResponseRedirect(reverse('register_view'))


# def mobile_login(request):
#     if request.method == "POST":
#         if "mobile" in request.POST:
#             mobile = request.POST.get('mobile')
#             user = MyUser.objects.get(mobile=mobile)
#             login(request, user)
#             return HttpResponseRedirect(reverse('dashboard'))
#


def dashboard(request):
    return render(request, 'dashboard.html')


def log_out(request):
    logout(request)
    return redirect('/')


def resend_otp(request, *args, **kwargs):
    yourmobile = kwargs['mobile']
    user1 = MyUser.objects.filter(mobile=yourmobile).first()
    # send otp
    if user1.is_block:
        return redirect("/")
    if not user1.is_block:
        otp = helper.get_random_otp()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        helper.send_otp(yourmobile, otp)
        # save otp
        print(otp)
        user1.otp = otp
        user1.save()
        return redirect(f'/verify/{yourmobile}')

    context = {

    }
    return render(request, 'verify.html', context)
