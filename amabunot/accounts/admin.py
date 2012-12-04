from django.contrib import admin
from accounts.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', '_name', '_email', 'department' ,'designation']
    list_filter  = ['user__is_active', 'designation']
    
    _name = lambda self, obj: obj.user and obj.user.get_full_name()
    _name.short_description = 'Full Name'
    _name.admin_order_field = 'user'

    _email = lambda self, obj: obj.user and obj.user.email
    _email.short_description = 'Email Address'
    _email.admin_order_field = 'user'

admin.site.register(UserProfile, ProfileAdmin)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['name','acronym','created','last_updated']
	list_filter  = ['name']
	
admin.site.register(Department, DepartmentAdmin)

class DesignationAdmin(admin.ModelAdmin):
	list_display = ['name','department','created','last_updated']
	list_filter  = ['department']
	
admin.site.register(Designation, DesignationAdmin)

class ContactInformationAdmin(admin.ModelAdmin):
	list_display = ['user','type','value']
	list_filter  = ['user']

admin.site.register(ContactInformation, ContactInformationAdmin)
