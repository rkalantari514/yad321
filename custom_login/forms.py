from django import forms


#
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = models.MyUser
#         fields = ['mobile', ]


class RegisterForm(forms.Form):
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':"×××××××××09" ,
           'maxlength':"11",
            'class': 'form-control'
        }
        ),
        label='موبایل'
    )

    condition = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'type' : "checkbox",
            'class':"required custom-control-input",
            'id':"customChecka1"

        }
        ),
    )



    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if mobile[0] != "0" or mobile[1] != "9" or len(mobile) !=11:
            raise forms.ValidationError('شماره موبایل اشتباه است')
        return mobile


class VerifyForm(forms.Form):
    yourotp = forms.IntegerField(
        widget=forms.TextInput(attrs={
           'class': 'form-control verify-input',
           'type' : "text",
           'placeholder':"...." ,
           'maxlength':"4"

        }),
        label='کد ارسال شده'
    )
    # def clean_yourotp(self,otp):
    #     yourotp=self.cleaned_data.get('yorotp')
    #     if yourotp != otp:
    #         raise forms.ValidationError('کد اشتباه است')
    #     return yourotp



