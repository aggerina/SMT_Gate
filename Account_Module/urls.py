from django.urls import  path
from Account_Module.views import RegisterView, LoginView, ActivateAccountView,ForgetPasswordView, ResetPasswordView, LogOutView
urlpatterns = [
    path('register', RegisterView.as_view(), name='Register_url'),
    path('login', LoginView.as_view(), name='Login_url'),
    path('logOut', LogOutView.as_view(), name='LogOut_url'),
    path('forget_pass', ForgetPasswordView.as_view(), name='Forgot_paasword_url'),
    path('reset_pass/<active_code>', ResetPasswordView.as_view(), name='Reset_paasword_url'),
    path('activate_account/<email_active_code>', ActivateAccountView.as_view(), name='Activate_Account_url'),
]

