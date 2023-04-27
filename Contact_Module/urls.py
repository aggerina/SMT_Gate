from django.urls import  path
from Contact_Module.views import ContactUs_view, CreateProfileView, Profile_ListView,About_UsView

urlpatterns = [
    # path('contact_us', Contact_Us, name='Contact_url')
    path('contact_us', ContactUs_view.as_view(), name='Contact_Page_url'),
    path('about_us', About_UsView.as_view(), name='About_us_url'),
    path('Profile', CreateProfileView.as_view(), name='Profile_url'),
    path('Profile_list', Profile_ListView.as_view(), name='Profile_list_url'),
]