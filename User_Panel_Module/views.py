from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from User_Panel_Module.forms import EditProfileModelForm, ChangePasswordForm
from Account_Module.models import User
from django.contrib.auth import logout
class UserPanerDashboard(TemplateView):
    template_name = 'User_panel_Module/User_Panle_Dashboard.html'


##render Partial
def UserPanel_Menu_Component(request: HttpRequest):
    current_user = User.objects.filter(id=request.user.id).first()
    context = {

        'current_user': current_user
    }

    return render(request,'Components/User_Panel_Menu_component.html', context)

class EditUserProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()

        # edit_form = EditProfileModelForm(initial={
        #     'first_name': current_user.first_name
        # })
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user':current_user
        }
        return  render(request, 'User_panel_Module/Edite_Panel_User.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        context = {
            'form': edit_form,
            'current_user':current_user
        }
        if edit_form.is_valid():
            edit_form.save(commit=True)
        return render(request, 'User_panel_Module/Edite_Panel_User.html', context)

class ChangePasswordView(View):
    def get(self, request: HttpRequest):

        context = {
            'Form': ChangePasswordForm
        }
        return render(request, 'User_panel_Module/change_password_page.html', context)
    def post(self, request: HttpRequest):
        Form = ChangePasswordForm(request.POST)
        if Form.is_valid():

            Current_User: User = User.objects.filter(id=request.user.id).first()
            if Current_User.check_password(Form.cleaned_data.get('Current_Password')):
                Current_User.set_password(Form.cleaned_data.get('New_Password'))
                Current_User.save()
                logout(request)
                return  redirect(reverse('LogOut_url'))
            else:
                Form.add_error('Current_Password', 'پسورد اشتباه میباشد ')


        context = {
            'Form': Form
        }
        return render(request, 'User_panel_Module/change_password_page.html', context)



