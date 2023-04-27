from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AccountModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Account_Module'
    verbose_name = _('Account Module')
