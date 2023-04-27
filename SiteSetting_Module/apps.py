from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SitesettingModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SiteSetting_Module'
    verbose_name = _('SiteSetting Module')
