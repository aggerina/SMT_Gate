from django.contrib import admin
from Account_Module.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name','about_user']

admin.site.register(User, UserAdmin)