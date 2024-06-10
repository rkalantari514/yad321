from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from mycity.models import City, State


class CreateMarasemForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان مراسم', 'class': 'form-control'}),
        label='عنوان مراسم'
    )



    state = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'استان', 'class': 'form-control custom-select'}),
        queryset=State.objects.all(),
        label='استان',
        # attrs={'placeholder': 'استان', 'class': 'form-control'},
    )



    city = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'شهر', 'class': 'form-control custom-select'}),
        queryset=City.objects.all(),
                                  label='شهر',
                                  )


    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'آدرس', 'class': 'form-control'}),
        label='آدرس'
    )

    event_date = forms.DateField(
        widget=forms.DateInput(),
        )

    starttime =forms.TimeField(
        widget=forms.TimeInput(attrs={'placeholder': 'زمان آغاز',
                                      'type':"time",
                                      'class':'form-control',
                                      'id' : "inputMDEx1",
                                                                     }),
        label='ساعت شروع'

    )

    finishtime =forms.TimeField(
        widget=forms.TimeInput(attrs={'placeholder': 'زمان پایان',
                                      'type':"time",
                                      'class':'form-control',
                                      'id' : "inputMDEx1",
                                                                     }),
        label='ساعت پایان'
    )




    def __init__(self, *args, **kwargs):
        super(CreateMarasemForm, self).__init__(*args, **kwargs)

        #111111111111111111111111111111111111111111111111
        # self.fields['event_date'] = JalaliDateField(label=('event_date'),  # date format is  "yyyy-mm-dd"
        #                                       widget=AdminJalaliDateWidget  # optional, to use default datepicker
        #                                       )
        #1111111111111111111111111111111111111111111111111111

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})


        #111111111111111111111111111111111111111111111111

        self.fields['event_date'] = JalaliDateField(label=('تاریخ مراسم'),
        # self.fields['event_date'] = SplitJalaliDateTimeField(label=('date time'),
        #                                                     widget=AdminSplitJalaliDateTime
                                                            widget=AdminJalaliDateWidget
                                                            # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
                                                            )
        # #111111111111111111111111111111111111111111111111





