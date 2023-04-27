from django.contrib import admin
from Contact_Module.models import ContactUs, UserProfile
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'full_name', 'message', 'created_date', 'response', 'is_read_by_admin']
    list_editable = ['is_read_by_admin']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['image']
admin.site.register(ContactUs, ContactUsAdmin)

admin.site.register(UserProfile, UserProfileAdmin)

