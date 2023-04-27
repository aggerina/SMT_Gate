from modeltranslation.translator import TranslationOptions, translator
from SiteSetting_Module.models import SiteSetting, FooterLink, FooterLinkBox, Slider, Navbar, About_EBusiness, WorkingWithUS


class SiteSettingTranslationOptions(TranslationOptions):
    fields = ['Site_Name', 'Address', 'About_us_Text', 'CopyRight', 'Our_Services', 'Our_Special_Team', 'Our_Portfolio','Price', 'About_eBusiness', 'WorkingWithUS','Latest_News', 'Send_Message']


translator.register(SiteSetting, SiteSettingTranslationOptions)


class FooterLinkTranslationOptions(TranslationOptions):
    fields = ['Title']


translator.register(FooterLink, FooterLinkTranslationOptions)


class FooterLinkBoxTranslationOptions(TranslationOptions):
    fields = ['Title']


translator.register(FooterLinkBox, FooterLinkBoxTranslationOptions)


class SliderTranslationOptions(TranslationOptions):
    fields = ['Title', 'Description']
translator.register(Slider, SliderTranslationOptions)

class NavbarTranslationOptions(TranslationOptions):
    fields = [ 'Home', 'About', 'Services','SalesProducts', 'Protfilo', 'Team', 'Blog', 'Contact', 'Account', 'Login', 'ForgotPassword', 'Logout','Register', 'Location', 'Email', 'Call']

translator.register(Navbar,NavbarTranslationOptions)


class About_EBusinessTranslator(TranslationOptions):
    fields = ['Description1', 'Description2', 'Description3' , 'Description4', 'Description5', 'Description6', 'Description7']
translator.register(About_EBusiness, About_EBusinessTranslator)

class WorkingWithUsTranslator(TranslationOptions):
    fields  = ['Description1', 'Description2']

translator.register(WorkingWithUS, WorkingWithUsTranslator)
