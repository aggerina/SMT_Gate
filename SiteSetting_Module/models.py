from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class SiteSetting(models.Model):
    Site_Name = models.CharField(max_length=200, verbose_name=_('Site Name'), blank=True, null=True,)
    Site_Url = models.URLField(max_length=200, verbose_name=_('Site Url'), blank=True, null=True,)
    Address = models.CharField(max_length=200, verbose_name=_('Address'), blank=True, null=True,)
    About_us_Text = models.TextField( verbose_name=_('About us Text'), blank=True, null=True)
    About_eBusiness = models.CharField( max_length=200, verbose_name=_('About_eBusiness'), blank=True, null=True)
    WorkingWithUS = models.CharField( max_length=200, verbose_name=_('WorkingWithUS'), blank=True, null=True)
    Latest_News = models.CharField( max_length=200, verbose_name=_('Latest_News'), blank=True, null=True)
    Location = models.URLField(max_length=600, verbose_name=_('Location'), blank=True, null=True)
    Phone_1 = models.CharField(max_length=15, verbose_name=_('Phone_1'), blank=True, null=True)
    Phone_2 = models.CharField(max_length=15, verbose_name=_('Phone_2'), blank=True, null=True)
    Fax = models.CharField(max_length=15, verbose_name=_('Fax'), blank=True, null=True)
    Email = models.CharField(max_length=20, verbose_name=_('Email'), blank=True, null=True)
    Site_Logo = models.ImageField(upload_to='images/SiteSetting/', verbose_name=_('Site Logo'))
    CopyRight = models.CharField(max_length=200, verbose_name=_('CopyRight'), blank=True, null=True,)

    is_main_setting = models.BooleanField(verbose_name=_('Main_setting'), blank=True, null=True)

    Price = models.CharField(max_length=15, verbose_name=_('Price'), blank=True, null=True)
    Our_Services = models.CharField(max_length=15, verbose_name=_('Our Services'), blank=True, null=True)
    Our_Special_Team = models.CharField(max_length=20, verbose_name=_('Our Special Team'), blank=True, null=True)
    Our_Portfolio = models.CharField(max_length=20, verbose_name=_('Our Portfolio'), blank=True, null=True)
    Send_Message = models.CharField(max_length=20, verbose_name=_('Send Message'), blank=True, null=True)

    class Meta:
        verbose_name = _('Site Setting')
        verbose_name_plural = _('Site Settings')


    def __str__(self):
        return self.Site_Name


class FooterLinkBox(models.Model):
    Title = models.CharField(verbose_name=_('Title'), max_length=200 )
    class Meta:
        verbose_name = _('Category of footer link')
        verbose_name_plural = _('Category of footer links')

    def __str__(self):
        return self.Title

class FooterLink(models.Model):
    Title = models.CharField(verbose_name=_('Title'), max_length=200 )
    Url = models.URLField(verbose_name=_('Url'), max_length=200)
    footer_link_box = models.ForeignKey(FooterLinkBox, on_delete=models.CASCADE ,verbose_name=_('Category of footer link'))
    class Meta:
        verbose_name = _('Footer link')
        verbose_name_plural = _('Footer links')

    def __str__(self):
        return self.Title


class Slider(models.Model):
    Title = models.CharField(max_length=30, verbose_name=_('Title'), blank=True, null=True)
    Url = models.URLField(max_length=100, verbose_name=_('Url'), blank=True, null=True)
    Urt_Title = models.CharField(max_length=100, verbose_name=_('Urt Title'), blank=True, null=True)
    Description = models.CharField(max_length=200, verbose_name=_('Description'), blank=True, null=True)
    Image = models.ImageField(upload_to='images/Silders', verbose_name=_('Image'))
    Is_Active =  models.BooleanField(verbose_name=_('Status '), default=True)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural =  _('Sliders')

    def __str__(self):
        return self.Title


class Navbar(models.Model):
    Title  = models.CharField(max_length=10, verbose_name=_('Navbar'), blank=True, null=True)
    Home  = models.CharField(max_length=10, verbose_name=_('Home'), blank=True, null=True)
    About  = models.CharField(max_length=10, verbose_name=_('About Us'), blank=True, null=True)
    Services  = models.CharField(max_length=10, verbose_name=_('Services'), blank=True, null=True)
    SalesProducts  = models.CharField(max_length=20, verbose_name=_('SalesProducts'), blank=True, null=True)
    Protfilo  = models.CharField(max_length=10, verbose_name=_('Protfilo'), blank=True, null=True)
    Team  = models.CharField(max_length=10, verbose_name=_('Team'), blank=True, null=True)
    Blog  = models.CharField(max_length=10, verbose_name=_('Blogs'), blank=True, null=True)
    Contact  = models.CharField(max_length=10, verbose_name=_('Contact'), blank=True, null=True)
    Account  = models.CharField(max_length=10, verbose_name=_('Account'), blank=True, null=True)
    Login  = models.CharField(max_length=10, verbose_name=_('Login'), blank=True, null=True)
    ForgotPassword  = models.CharField(max_length=20, verbose_name=_('ForgotPassword'), blank=True, null=True)
    Logout  = models.CharField(max_length=10, verbose_name=_('Logout'), blank=True, null=True)
    Register  = models.CharField(max_length=10, verbose_name=_('Register'), blank=True, null=True)
    Our_Services  = models.CharField(max_length=15, verbose_name=_('Our Services'), blank=True, null=True)
    Location  = models.CharField(max_length=15, verbose_name=_('Location'), blank=True, null=True)
    Email  = models.CharField(max_length=15, verbose_name=_('Email'), blank=True, null=True)
    Call  = models.CharField(max_length=15, verbose_name=_('Call'), blank=True, null=True)

    class Meta:
        verbose_name = _('Navbar')
        verbose_name_plural =  _('Navbars')
    def __str__(self):
        return self.Title



class About_EBusiness(models.Model):
    Description1 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_1'), blank=True , null=True)
    Description2 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_2'), blank=True , null=True)
    Description3 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_3'), blank=True , null=True)
    Description4 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_4'), blank=True , null=True)
    Description5 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_5'), blank=True , null=True)
    Description6 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_6'), blank=True , null=True)
    Description7 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_6'), blank=True , null=True)
    Image = models.ImageField(upload_to='images/Ebout',null=True, verbose_name=_('Image'))


    def __str__(self):
        return self.Description1

class WorkingWithUS(models.Model):
    Description1 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_1'), blank=True , null=True)
    Description2 = models.CharField(max_length=200, default='', verbose_name=_('توضیحات_2'), blank=True , null=True)

    Image = models.ImageField(upload_to='images/Ebout',null=True, verbose_name=_('Image'))


    def __str__(self):
        return self.Description1






