
from django.contrib import admin
from django.urls import path, include
from Home_Module import views

urlpatterns = [

    path('',views.HomeView.as_view(), name='Home_Page_Url'),
    # path('countact_us',views.Contect_Page, name='Contact_Page_url'),
    # path('Site_Header', views.Site_header_Partial, name='site_header-Partial'),

]