from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout

from Account_Module.forms import RegisterForm, LoginForm,ForgotPasword_Form, ResetPasword_Form
from  utils.EmailService import SendEmail

# class RegisterView(View):
#     def get(self, request):
#         register_form = RegisterForm()
#         context = {
#             'register_form': register_form
#         }
#
#         return render(request, 'Acount_module/register.html', context)
#
#     def post(self, request):
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             user_email = register_form.cleaned_data.get('email')
#             user_password = register_form.cleaned_data.get('password')
#             user: bool = User.objects.filter(email__iexact=user_email).exists()
#             if user:
#                 register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
#             else:
#                 new_user = User(
#                     email=user_email,
#                     email_active_code=get_random_string(72),
#                     is_active=False,
#                     username=user_email)
#                 new_user.set_password(user_password)
#                 new_user.save()
#                 # todo: send email active code
#                 SendEmail('فعال سازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/active_account.html')
#                 return redirect(reverse('Login_url'))
#
#         context = {
#             'register_form': register_form
#         }
#
#         return render(request, 'Acount_module/register.html', context)
#


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Acount_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                SendEmail('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/active_account.html')
                return redirect(reverse('Login_url'))

        context = {
            'register_form': register_form
        }

        return render(request, 'Acount_module/register.html', context)

class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('Login_url'))
            else:
                # todo: show your account was activated message to user
                pass

        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }


        return render(request, 'Acount_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('DashboardUser_Url'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'Acount_module/login.html', context)



class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forgot_password_form = ForgotPasword_Form()
        return render(request, 'Acount_module/ForgotPassword.html', {'forgot_password_form':forgot_password_form})

    def post(self, request: HttpRequest):
        forgot_password_form = ForgotPasword_Form(request.POST)
        if forgot_password_form.is_valid():
            user_email = forgot_password_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                SendEmail('فعالسازی حساب کاربری', user.email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('Home_Page_Url'))




        context = {'forgot_password_form':forgot_password_form}
        return render(request, 'Acount_module/ForgotPassword.html', context)




class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('Login_url'))
        reset_password_form = ResetPasword_Form()

        context = {'reset_password_form': reset_password_form,
                   'user':user}
        return render(request, 'Acount_module/ResetPassword.html', context)



    def post(self, request: HttpRequest, active_code):
        reset_password_form = ResetPasword_Form(request.POST)
        if reset_password_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return redirect(reverse('Login_url'))

            user_new_Pass = reset_password_form.cleaned_data.get('password')
            user.set_password(user_new_Pass)
            user.email_active_code = get_random_string(72)
            user.is_active =True
            user.save()

        context = {'reset_password_form': reset_password_form}
        return redirect(reverse('Login_url'))


class LogOutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(reverse('Login_url'))



