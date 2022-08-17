from django.contrib import admin
from website.models import Contact

# Register your models here.
class Admin_ContactCustomizations(admin.ModelAdmin):
    date_hierarchy = "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': (("Name", "Email"), ("Subject", "Message"))
        }),
        ('Advanced options', {
            'classes': ('wide', 'collapse', 'extrapretty'),
            'fields': ("Created_Date", "Updated_Date"),
        }),
    )
    list_display= ("Name", "Subject", "Email" ,"Created_Date")
    list_filter= ("Subject", "Created_Date")
    search_fields= ["Name", "Subject", "Message"]
    
admin.site.register(Contact, Admin_ContactCustomizations)