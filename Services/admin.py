from django.contrib import admin

from Services.models import Service, Team


class AdminServices(admin.ModelAdmin):
    list_display = ['Title', 'ShortDescription', 'Description', 'Create_Date',]
    filter_horizontal = ['slider']
admin.site.register(Service, AdminServices)


class AdminTeam(admin.ModelAdmin):
    list_display = ['Title', 'ShortDescription', 'Description']
admin.site.register(Team, AdminTeam)


