from django.db import models
from Account_Module.models import User
from jalali_date import datetime2jalali , date2jalali
from django.utils.translation import gettext_lazy as _
# Create your models here.

class NewsCategory(models.Model):
    parent = models.ForeignKey('NewsCategory', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name=_('Parent'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    url_title = models.CharField(max_length=200, unique=True, verbose_name=_('Url title'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activated'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('NewsCategory')
        verbose_name_plural = _('NewsCategorys')


class News(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('Title'))
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name=_('Slug'))
    image = models.ImageField(upload_to='images/News', verbose_name=_('Image'))
    short_description = models.TextField(verbose_name=_('Short_description'))
    text = models.TextField(verbose_name=_('Text'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    selected_categories = models.ManyToManyField(NewsCategory, verbose_name=_('Choices category'))
    Author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'), null=True, editable=False)
    Create_Date = models.DateTimeField(verbose_name=_('Create_Date'), editable=False, auto_now_add=True, blank=True, null=True)


    def ge_jalali_create_date(self):
        return date2jalali(self.Create_Date)
    def ge_jalali_create_time(self):
        return self.Create_Date.strftime('%H:%M')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News list')


class NewsComment(models.Model):
    News = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('News'))
    parent = models.ForeignKey('NewsComment',null=True, blank=True,  on_delete=models.CASCADE, verbose_name=_('Parent'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Parent'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('create_date'))
    text = models.TextField(verbose_name=_('Text'))

    def ge_jalali_create_date(self):
        return date2jalali(self.create_date)
    def ge_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
    def __str__(self):
        return str(self.user)