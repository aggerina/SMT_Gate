from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ContactModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Contact_Module'
    verbose_name = _('Module Contact Us')

