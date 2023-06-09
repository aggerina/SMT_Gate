# Generated by Django 4.1.5 on 2023-02-04 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='Image')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='Short description')),
                ('description', models.TextField(db_index=True, verbose_name='Main description')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=300, verbose_name='Title')),
                ('Is_active', models.BooleanField(verbose_name='Is_active')),
            ],
            options={
                'verbose_name': 'ProductBrand',
                'verbose_name_plural': 'ProductBrands',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='Title')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='url on title')),
                ('is_active', models.BooleanField(verbose_name='is_active')),
                ('is_delete', models.BooleanField(verbose_name='is_delete')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categorys',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='Product_Module.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product_Module.productbrand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='Product_Module.productcategory', verbose_name='Product Categorys'),
        ),
    ]
