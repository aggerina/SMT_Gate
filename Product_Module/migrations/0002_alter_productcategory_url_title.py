# Generated by Django 4.1.5 on 2023-04-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='url_title',
            field=models.SlugField(max_length=300, verbose_name='url on title'),
        ),
    ]