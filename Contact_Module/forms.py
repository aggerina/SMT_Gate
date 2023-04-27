from    django import forms
from Contact_Module.models import ContactUs
from django.utils.translation import gettext_lazy as _
# class ContactForm(forms.Form):
#     full_name = forms.CharField(label='نام و نام خانوادگی',
#                                 max_length=50,
#                                 error_messages={
#                                     'required': 'نام و نام خانوادگی را درست وارد کنید ',
#                                     'max_length':'نام و نام خانوادگی نمی توتند از 50 کاراکتر بیشتر باشد '},
#                                 widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label='ایمیل',max_length=50)
#     subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='موضوع', max_length=40)
#     message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="متن پیام ",max_length=400)
#


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'title', 'email', 'message']
        # exclude = ['response']
        # fields = ['__all__']
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':_('full name')}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':_('title')}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':_('email')}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':_('message')}),
            # 'TestDate': forms.DateTimeField(attrs={'class':'form-control'}),
        }
        labels ={
            'full_name': _('full_name')
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی شما باید وارد شود '
            }
        }


class ProfileForm(forms.Form):
    # User_image = forms.FileField()
    User_image = forms.ImageField()