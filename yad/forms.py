from django import forms


# @login_required(login_url='/register')
#     fields = ['title','name','family','death_time','city','description','master_image','favio_image']
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from mycity.models import State, City


class CreateYadForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'عنوان (مرحوم / مرحومه)', 'class': 'form-control'}),
        label='عنوان'
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
        label='نام'
    )

    family = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control'}),
        label='نام خانوادگی'
    )

    death_date = forms.DateField(
        widget=forms.DateInput(

        ),
    )

    description=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'توضیحات', 'class': 'form-control'}),
        label='توضیحات'
    )

    state = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'استان','class': 'form-control custom-select'}),
        queryset=State.objects.all(),
        label='استان',
        # attrs={'placeholder': 'استان', 'class': 'form-control'},
    )

    city = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'شهر', 'class': 'form-control custom-select'}),
        queryset=City.objects.all(),
                                  label='شهر',
                                  )

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'placeholder': 'تصویر پروفایل',
            'type': 'file',
            'id': 'fileuploadInput',
            'accept': '.png, .jpg, .jpeg'
        }
        ),
        label='تصویر پروفایل'
    )










    def clean(self):
        print("----------------it is clean")



    def __init__(self, *args, **kwargs):
        super(CreateYadForm, self).__init__(*args, **kwargs)
        self.fields['death_date'] = JalaliDateField(label=(' تاریخ فوت / شهادت'),
                                                            widget=AdminJalaliDateWidget(
                                                                # attrs={'class': 'form-control'},
                                                            )
                                                            )


