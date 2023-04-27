from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from Contact_Module.forms import  ContactUsModelForm, ProfileForm
from  Contact_Module.models import ContactUs, UserProfile
from django.views import  View
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView, TemplateView
from django.http import HttpRequest
from SiteSetting_Module.models import SiteSetting, Navbar


class ContactUs_view(CreateView):

    model = ContactUs
    template_name = 'Contact_Modul/contact_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact/contact_us'
    def get_context_data(self,  **kwargs):

        context =  super().get_context_data( **kwargs)
        Site_Setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        navbar = Navbar.objects.first()

        context['Site_Setting'] = Site_Setting
        context['Navbar'] = navbar
        return context

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)



class CreateProfileView(CreateView):
    template_name = 'Contact_Modul/Create_Profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/Profile'


class Profile_ListView(ListView):
    model = UserProfile
    template_name = "Contact_Modul/Profile_ListView.html"
    context_object_name = 'Profiles'


class About_UsView(TemplateView):
    template_name = 'Contact_Modul/About_us.html'
    def get_context_data(self, **kwargs):
        context  = super(About_UsView , self ).get_context_data(**kwargs)
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()

        context['site_setting'] = site_setting
        return context


#
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#
#         return render(request,'Contact_Module/Create_Profile.html', {
#             'form':form
#         })
#
#     def post(self, request):
#         print(request.FILES)
#         print(request.POST)
#         submited_form = ProfileForm(request.POST, request.FILES )
#         if submited_form.is_valid():
#             profile = UserProfile(image=request.FILES['User_image'])
#             profile.save()
#             return redirect('Profile_url')
#
#         return render(request,'Contact_Module/Create_Profile.html', {
#             'form': submited_form
#         })
#

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#
#         return render(request,'Contact_Module/Create_Profile.html', {
#             'form':form
#         })
#
#     def post(self, request):
#         print(request.FILES)
#         print(request.POST)
#         submited_form = ProfileForm(request.POST, request.FILES )
#         if submited_form.is_valid():
#             store_file(request.FILES['User_image'])
#             return redirect('Profile_url')
#
#         return render(request,'Contact_Module/Create_Profile.html', {
#             'form': submited_form
#         })


def store_file(file):
    with open('temp/image-1.png', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
        dest.close()
# #
# class  ContactUs_view(FormView):
#     template_name = 'Contact_Module/Contact_Us.html'
#     form_class =  ContactUsModelForm
#     success_url = '/contact_us'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#

#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#
#             contact_form.save()
#             return redirect('Home_Page')
#
#         context = {
#             'Contact_us_form': contact_form
#         }
#         return render(request, 'Contact_Module/Contact_Us.html', context)

# class  ContactUs_view(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         context = {
#             'Contact_us_form': contact_form
#         }
#         return render(request, 'Contact_Module/Contact_Us.html', context)
#
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#
#             contact_form.save()
#             return redirect('Home_Page')
#
#         context = {
#             'Contact_us_form': contact_form
#         }
#         return render(request, 'Contact_Module/Contact_Us.html', context)


# def Contact_Us(request):
#
#
#     if request.method == 'POST':
#         # contact_form = ContactForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#
#             # contact = ContactUs(
#             #     title= contact_form.cleaned_data['title'],
#             #     email  = contact_form.cleaned_data['email'],
#             #     full_name  = contact_form.cleaned_data['full_name'],
#             #     message  = contact_form.cleaned_data['message'],
#             #     is_read_by_admin= False,
#             # )
#             # contact.save()
#             contact_form.save()
#             return redirect('Home_Page')
#
#     else:
#         # contact_form = ContactForm()
#         contact_form = ContactUsModelForm()
#
#     context = {
#         'Contact_us_form': contact_form
#     }
#
#     return render(request, 'Contact_Module/Contact_Us.html', context)
