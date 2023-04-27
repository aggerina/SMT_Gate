from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Product_Module'
    verbose_name =_('Product Module')
