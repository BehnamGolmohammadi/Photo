from django.contrib import admin
from website.models import Contact, NewsLetter

# Register your models here.
class Admin_ContactCustomizations(admin.ModelAdmin):
    date_hierarchy = "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': (("First_Name", "Last_Name"), ("Email"), ("Subject", "Message"))
        }),
        # ('Advanced options', {
        #     'classes': ('wide', 'collapse', 'extrapretty'),
        #     'fields': ("Created_Date", "Updated_Date"),
        # }),
    )
    list_display= ("First_Name", "Last_Name", "Subject", "Email" ,"Created_Date")
    list_filter= ("Subject", "Created_Date")
    search_fields= ["First_Name", "Last_Name", "Subject", "Message"]
    
admin.site.register(Contact, Admin_ContactCustomizations)
admin.site.register(NewsLetter)