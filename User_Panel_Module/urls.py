from django.urls import path
from User_Panel_Module.views import UserPanerDashboard,EditUserProfile, ChangePasswordView

urlpatterns = [
    path('dashboard/', UserPanerDashboard.as_view(), name='DashboardUser_Url'),
    path('Edit_Profile/', EditUserProfile.as_view(), name='EditUserProfile_Url'),
    path('change_Password/', ChangePasswordView.as_view(), name='ChangePassword_Url'),
]