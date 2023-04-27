from django.contrib import admin
from django.http import HttpRequest

from . import models


# Register your models here.
from Article_Module.models import  Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active',]
    list_editable = ['url_title', 'parent', 'is_active']

class ArticelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'Author', 'Create_Date']
    list_editable = ['is_active']
    def save_model(self, request: HttpRequest, obj: Article , form, change):
        print("change: ", change)
        print("change: ", request.user)
        print("change: ", obj)
        print("change: ", request)
        obj.Author = request.user

        return super().save_model(request,obj,form,change)

class AdminArticleComment(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'parent']

admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticelAdmin)
admin.site.register(models.ArticelComment, AdminArticleComment)

