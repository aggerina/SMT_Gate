# Generated by Django 4.1.5 on 2023-04-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting_Module', '0002_navbar_salesproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='SalesProducts_en',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='SalesProducts'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='SalesProducts_fa',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='SalesProducts'),
        ),
    ]
