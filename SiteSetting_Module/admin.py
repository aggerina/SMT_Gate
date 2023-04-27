from django.contrib import admin

from  SiteSetting_Module.models import  *


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'Site_Url', 'Address', 'About_us_Text', 'Location', 'Phone_1', 'Phone_2', 'Fax', 'Email', 'Site_Logo', 'is_main_setting']

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Url']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Url', 'Urt_Title', 'Description', 'Image', 'Is_Active']
    list_editable = ['Url', 'Is_Active']

# class NavbarAdmin(admin.ModelAdmin):
    # list_display = [ 'About', 'Services', 'Protfilo', 'Team', 'Blog', 'Contact', 'Account', 'Login', 'ForgotPassword', 'Logout']

    # list_editable = [ 'About', 'Services', 'Protfilo', 'Team', 'Blog', 'Contact', 'Account', 'Login', 'ForgotPassword', 'Logout']

# class About_EBisness(admin.ModelAdmin):
#
admin.site.register(Navbar)
admin.site.register(SiteSetting)
admin.site.register(FooterLinkBox)
admin.site.register(Slider, SliderAdmin)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(About_EBusiness)
admin.site.register(WorkingWithUS)