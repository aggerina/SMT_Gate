"""CyberGate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home_Module import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [path('i18n/', include('django.conf.urls.i18n')),]
urlpatterns += i18n_patterns(
    path('', include('Home_Module.urls')),
    # path('', include('Contact_Module.urls')),
    path('Account/', include('Account_Module.urls')),
    path('user/', include('User_Panel_Module.urls')),
    path('contact/', include('Contact_Module.urls')),
    path('articles/', include('Article_Module.urls')),
    path('News/', include('News_Module.urls')),
    path('admin/', admin.site.urls ),
    path('Products/', include('Product_Module.urls' )),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

