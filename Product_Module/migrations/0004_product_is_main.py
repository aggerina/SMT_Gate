# Generated by Django 4.1.5 on 2023-04-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0003_product_description_en_product_description_fa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='اصلی / فرعی '),
        ),
    ]