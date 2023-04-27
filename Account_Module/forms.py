from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(

        widget=forms.EmailInput(attrs={'class':'form-control ', 'id':'floatingInput','placeholder':'name@example.com'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

    password = forms.CharField(

        widget=forms.PasswordInput(attrs={'class':'form-control ', 'id':'floatingInputpass','placeholder':'Password'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


    confirm_password = forms.CharField(

        widget=forms.PasswordInput(attrs={'class':'form-control ', 'id':'floatingInputConfPass','placeholder':'Confrim'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class LoginForm(forms.Form):
    email = forms.EmailField(

        widget=forms.EmailInput(attrs={'class':'form-control ', 'id':'floatingInput','placeholder':'name@example.com'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class':'form-control ', 'id':'floatingInputpass','placeholder':'Password'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )




class ForgotPasword_Form(forms.Form):
    email = forms.EmailField(

        widget=forms.EmailInput(attrs={'class':'form-control ', 'id':'floatingInput','placeholder':'name@example.com'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )



class ResetPasword_Form(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
