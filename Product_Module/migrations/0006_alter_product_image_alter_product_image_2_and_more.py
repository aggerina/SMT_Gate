# Generated by Django 4.1.5 on 2023-04-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0005_product_image_2_product_image_3_product_image_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='-', upload_to='images/products', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default='-', upload_to='images/products', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(default='-', upload_to='images/products', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(default='-', upload_to='images/products', verbose_name='Image'),
        ),
    ]
