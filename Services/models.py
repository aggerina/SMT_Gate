from django.db import models
from django.utils.translation import gettext_lazy as _

from SiteSetting_Module.models import Slider


class Service(models.Model):
    Title = models.CharField(max_length=30, verbose_name=_('Title'))
    ShortDescription = models.CharField(max_length=50, verbose_name=_('Short Description'))
    Description = models.TextField(verbose_name=_('Description'))
    Create_Date = models.DateTimeField(auto_now_add=True, verbose_name=_('Create Date'))
    slider = models.ManyToManyField(Slider, verbose_name=_('Slider'))
    def __str__(self):
        return '__-----'
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')



class Team(models.Model):
    Title = models.CharField(max_length=30, verbose_name=_('Title'))
    ShortDescription = models.CharField(max_length=50, verbose_name=_('Short Description'))
    Description = models.TextField(verbose_name=_('Description'))
    Image = models.ImageField(upload_to='images/Teams', verbose_name=_('اواتار '))
    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


