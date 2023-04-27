from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField( max_length=20,null=True, blank=True,   verbose_name=_('Mobile'))
    avatar = models.ImageField(upload_to="images/Profiles", max_length=100, verbose_name=_('Avatar'), blank=True, null=True)
    email_active_code = models.CharField(max_length=100, verbose_name=_('email active code'))
    about_user = models.TextField(null=True, blank=True,verbose_name=_('About User'))
    address = models.TextField(blank=True, null=True, verbose_name=_('Address'))

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        if self.first_name is not  '' and self.last_name is not '':
            return self.get_full_name()
        else:
            return self.email
