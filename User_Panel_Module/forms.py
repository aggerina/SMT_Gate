# from  Account_Module.models import User
# from django import forms
# class EditeProfile_Form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'avatar', 'address']
#         # exclude = ['response']
#         # fields = ['__all__']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class':'form-control'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control'}),
#             'avatar': forms.ImageField(),
#             'address': forms.Textarea(attrs={'class':'form-control'}),
#             # 'TestDate': forms.DateTimeField(attrs={'class':'form-control'}),
#         }
#         labels ={
#             'full_name': 'نام',
#             'last_name': 'نام خانوادگی',
#             'avatar': 'عکس شما',
#             'address': 'ادرس  شما',
#
#         }
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from Account_Module.models import User
class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar','about_user', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                # 'rows': 3,
                # 'id': 'message'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                # 'rows': 3,
                # 'id': 'message'
            })
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'about_user': 'درباره کاربر',
            'address': 'آدرس',
        }


class ChangePasswordForm(forms.Form):
    Current_Password = forms.CharField(
        label='کلمه عبور فعلی ',
        widget=forms.PasswordInput(attrs={
            'class':'form-control'
        }
    ))
    New_Password = forms.CharField(

    label='کلمه عبور جدید ',
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }),
    validators=[
        validators.MaxLengthValidator(16),
    ]
    )

    Confirm_Password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class':'form-control'
        }),
        validators=[
            validators.MaxLengthValidator(16),
        ]
    )

    def clean_Confirm_Password(self):
        New_Password = self.cleaned_data.get('New_Password')
        Confirm_Password = self.cleaned_data.get('Confirm_Password')
        if New_Password == Confirm_Password:
            return Confirm_Password
        else:
            raise ValidationError('کلمه عبور جدید با تکرار کلمه عبور مقایرت دارد ')
