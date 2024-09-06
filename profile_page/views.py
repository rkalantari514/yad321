from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from custom_login.models import MyUser
from profile_page.forms import EditProfileForm
from yad.models import Yad


def profilepage (request, *args, **kwargs):
    profileId= kwargs['profileId']
    profile_user=MyUser.objects.filter(id=profileId).first()
    print(profileId)
    print(profile_user)
    profilename=profile_user.profile_name
    print(profilename)
    profilepic=profile_user.profile_pic
    print('---------------------------------')
    yadbood1=Yad.objects.filter(owner=profile_user).order_by('death_date')
    yadbood2=Yad.objects.filter(reyad=profile_user).order_by('death_date')


    profilesalavat=0
    profilequran=0
    profilefatehe=0
    for yad in yadbood1:
        profilesalavat += yad.salavat_count
        profilefatehe += yad.fatehe_count
        profilequran +=yad.quran_count



    try:
        user=request.user
    except:
        pass


    # profile_id=kwargs['profileId']
    # profile_user=MyUser.objects.filter(id=profile_id).first()


    can_edit_profile= user == profile_user



    edit_form = EditProfileForm(request.POST or None,request.FILES or None ,
                                  initial={
                                      'profile_name': profile_user.profile_name,
                                      'profile_pic': profile_user.profile_pic,
                                      'profile_bio':profile_user.profile_bio},

                                                                )
    ptitle=profilename
    context = {
        'myyad': yadbood1,
        'otheryad': yadbood2,
        'profilename': profilename,
        'profilepic': profilepic,
        'profilesalavat': profilesalavat,
        'profilefatehe': profilefatehe,
        'profilequran': profilequran,
        'edit_form': edit_form,
        'profile_user': profile_user,
        'can_edit_profile': can_edit_profile,
        'title': ptitle
    }



    if edit_form.is_valid():
        profile_name = edit_form.cleaned_data.get('profile_name')
        profile_pic=edit_form.cleaned_data.get('profile_pic')
        profile_bio=edit_form.cleaned_data.get('profile_bio')

        user.profile_name= profile_name
        user.profile_pic=profile_pic
        user.profile_bio=profile_bio
        user.save()
        return redirect (f'/profile/{profileId}')

    smsandroid=f"sms:?body=سلام لطفا از صفحات یادبود مجازی  {profilename} دیدن فرمایید.www.yadeo.ir/profile/{profileId}"
    smsforios=f"sms:&body=سلام لطفا از صفحه یادبود مجازی  {profilename}  دیدن فرمایید.www.yadeo.ir/profile/{profileId}"
    telegram=f"https://telegram.me/share/url?url=http://yadeo.ir/profile/{profileId}"
    whatsapp=f"whatsapp://send?text=http://yadeo.ir/profile/{profileId}"
    eitaa=f"https://eitaa.com/share/url?url=http://yadeo.ir/profile/{profileId}"
    bale=f"bale://share?text=http://yadeo.ir/profile/{profileId}"
    sorosh=f"soroush://share?text=http://yadeo.ir/profile/{profileId}"





    context = {
        'myyad': yadbood1,
        'otheryad': yadbood2,
        'profilename': profilename,
        'profilepic': profilepic,
        'profilesalavat': profilesalavat,
        'profilefatehe': profilefatehe,
        'profilequran': profilequran,
        'edit_form': edit_form,
        'profile_user': profile_user,
        'can_edit_profile': can_edit_profile,
        'title': ptitle,
        'smsandroid': smsandroid,
        'smsforios': smsforios,
        'telegram': telegram,
        'whatsapp': whatsapp,
        'eitaa': eitaa,
        'bale': bale,
        'sorosh': sorosh
    }



    return render(request, 'profile/profile_page.html',context)



# @login_required(login_url='/register')
# def EditProfile(request,*args,**kwargs):
#     user_id = request.user.id
#     user = MyUser.objects.get(id=user_id)
#
#     profile_id=kwargs['profileId']
#     profile_user=MyUser.objects.filter(id=profile_id).first()
#
#     print(user)
#     print(user.profile_name)
#
#
#     if user is None or user != profile_user:
#         raise Http404('کاربر مورد نظر یافت نشد')
#
#     edit_form = EditProfileForm(request.POST ,request.FILES or None ,
#                                   initial={
#                                       'profile_name': profile_user.profile_name,
#                                       'profile_pic': profile_user.profile_pic},
#
#                                                                 )
#
#     context = {
#         'edit_form': edit_form,
#         'profile_user': profile_user,
#     }
#
#
#     if edit_form.is_valid():
#         profile_name = edit_form.cleaned_data.get('profile_name')
#         profile_pic=edit_form.cleaned_data.get('profile_pic')
#         user.profile_name= profile_name
#         user.profile_pic=profile_pic
#         user.save()
#
#     context = {
#         'edit_form': edit_form,
#         'profile_user': profile_user,
#     }
#     return render(request, 'profile/edit_profile.html', context)



