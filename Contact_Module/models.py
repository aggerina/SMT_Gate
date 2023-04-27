from django.db import models
from django.utils.translation import  gettext_lazy as _

# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    email = models.EmailField(max_length=300, verbose_name=_('email'))
    full_name = models.CharField(max_length=300, verbose_name=_('full_name'))
    message = models.TextField(verbose_name=_('message'))
    created_date = models.DateTimeField(verbose_name=_('created_date'), auto_now_add=True)
    response = models.TextField(verbose_name=_('response'), null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name=_('is_read_by_admin'), default=False)
    # TestDate = models.DateTimeField(verbose_name="تاریخ تست ")

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us list')

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # image = models.FileField(upload_to='images')
    image = models.ImageField(upload_to='images')