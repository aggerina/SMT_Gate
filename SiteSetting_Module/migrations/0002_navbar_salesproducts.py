# Generated by Django 4.1.5 on 2023-04-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting_Module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='SalesProducts',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='SalesProducts'),
        ),
    ]
