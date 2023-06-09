# Generated by Django 4.1.5 on 2023-02-04 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_fa', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('url_title', models.CharField(max_length=200, unique=True, verbose_name='Url title')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activated')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Article_Module.articlecategory', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'ArticleCategory',
                'verbose_name_plural': 'ArticleCategorys',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('title_fa', models.CharField(max_length=300, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=300, null=True, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='images/articles', verbose_name='Image')),
                ('short_description', models.TextField(verbose_name='Short_description')),
                ('short_description_fa', models.TextField(null=True, verbose_name='Short_description')),
                ('short_description_en', models.TextField(null=True, verbose_name='Short_description')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_fa', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('Create_Date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_Date')),
                ('Author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('selected_categories', models.ManyToManyField(to='Article_Module.articlecategory', verbose_name='Choices category')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticelComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create_date')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_fa', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article_Module.article', verbose_name='Article')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Article_Module.articelcomment', verbose_name='Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
