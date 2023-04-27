from django.db.models import Q
from django.shortcuts import render

from News_Module.models import News
from Services.models import Service
from  SiteSetting_Module.models import *
from Product_Module.models import Product, ProductCategory
# Create your views here.
from django.views import View
from  django.views.generic import TemplateView
from SiteSetting_Module.models import SiteSetting, Slider, Navbar
#
# def Index_Page(request):
#
#     return  render(request, 'home_modules/index_Page.html')


# class HomeView(View):
#     def get(self,request):
#         return render(request, 'home_modules/index_Page.html')

class HomeView(TemplateView):
    template_name = 'home_modules/index_Page.html'
    def get_context_data(self, **kwargs):
        context =   super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.filter(Is_Active=True)
        context['SiteSetting'] = SiteSetting.objects.all().first()
        context['navbar'] = Navbar.objects.all().first()
        context['Services'] = Service.objects.all()
        context['News'] = News.objects.all()
        context['About_EBusiness'] = About_EBusiness.objects.all().first()
        context['WorkingWithUS'] = WorkingWithUS.objects.all().first()
        context["Products"] = Product.objects.filter(Q(is_active=True) and Q(is_main=True))
        context["Categorys"] = ProductCategory.objects.filter(is_active=True)
        #
        #
        # for p in Product.objects.filter(Q(is_active=True) and Q(is_main=True)):
        #
        #     print(p.category.prefetch_related().first().url_title)
        #     for c in ProductCategory.objects.filter(is_active=True):
        #         pass
        #

                    # print(p.title, "++++++", c.title)

        # for  productCategurys in ProductCategory.objects.filter(is_active=True):
        #     print(productCategurys.url_title)


        return  context



# def Contect_Page(request):
#     Site_Setting: SiteSetting  = SiteSetting.objects.filter(is_main_setting=True).first()
#
#     context = {
#         'Site_Setting':Site_Setting,
#
#     }
#
#     return  render(request, 'home_modules/contact_page.html', context)

def Site_header_Component(request):
    Site_Setting: SiteSetting  = SiteSetting.objects.filter(is_main_setting=True).first()
    NavBar: Navbar  = Navbar.objects.all().first()
    productcategory: ProductCategory = ProductCategory.objects.filter(is_active=True)
    context = {
        'Site_Setting':Site_Setting,
        'NavBar':NavBar,
        'Productcategory': productcategory
    }

    return  render(request, 'shared/Site_Header_Partial.html', context)


def Site_Footer_Component(request):
    Site_Setting: SiteSetting  = SiteSetting.objects.filter(is_main_setting=True).first()
    navBar :Navbar = Navbar.objects.all().first()
    FooterLink_Boxes = FooterLinkBox.objects.all()
    for item in FooterLink_Boxes:
        item.footerlink_set

    context = {
        "FooterLink_Boxes":FooterLink_Boxes,
        'Site_Setting':Site_Setting,
        'NavBar':navBar,
    }

    return  render(request, 'shared/Site_Footer_Partial.html', context)