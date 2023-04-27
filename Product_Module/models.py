import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name=_('Title'))
    url_title = models.SlugField(max_length=300, db_index=True, verbose_name=_('url on title'))
    is_active = models.BooleanField(verbose_name=_('is_active'))
    is_delete = models.BooleanField(verbose_name=_('is_delete'))

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'
    def get_absolute_url(self):
        return reverse("ProductCategory_list_Url", kwargs={"slug": self.url_title})

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categorys')


class ProductBrand(models.Model):
    Title = models.CharField(blank=True,   max_length=300, verbose_name=_('Title'))
    Is_active = models.BooleanField(verbose_name=_('Is_active'))

    class Meta:
        verbose_name =_('ProductBrand')
        verbose_name_plural = _('ProductBrands')

    def __str__(self):
        return self.Title






class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('Title'))
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name=_('Product Categorys'))
    image = models.ImageField(upload_to='images/products',default='-', blank=False, null=False , verbose_name=_('Image'))
    image_2 = models.ImageField(upload_to='images/products',default='-',  blank=False, null=False , verbose_name=_('Image'))
    image_3 = models.ImageField(upload_to='images/products',default='-',  blank=False, null=False , verbose_name=_('Image'))
    image_4 = models.ImageField(upload_to='images/products',default='-',  blank=False, null=False , verbose_name=_('Image'))

    brand = models.ForeignKey( ProductBrand, on_delete=models.CASCADE, verbose_name=_('Brand'), null=True, blank=True)
    price = models.IntegerField(verbose_name=_('Price'))
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name=_('Short description'))
    description = models.TextField(verbose_name=_('Main description'), db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name=_('Slug'))
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    is_main = models.BooleanField(default=False, verbose_name='اصلی / فرعی ')
    Last_Update_Time = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now(), verbose_name=_('Last_Update_Time'))


    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        # return f"{self.title} ({self.price})"
        return f"تست"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption
