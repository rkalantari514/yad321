from django import forms
from django.core import validators


class EditProfileForm(forms.Form):
    profile_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'نام پروفایل', 'class': 'form-control'}),
        label='نام پروفایل'
    )

    profile_bio = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'بیوگرافی', 'class': 'form-control'}),
        label='بیوگرافی'
    )


    profile_pic = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'placeholder': 'تصویر پروفایل',
            'type':'file',
            'id':'fileuploadInput',
            'accept':'.png, .jpg, .jpeg'
        }
        ),
        label='تصویر پروفایل'
    )




