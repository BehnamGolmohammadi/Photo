from django.contrib import admin
from blog.models import Contact, Post, Category


# Register your models here.
class Admin_PostCustomizations(admin.ModelAdmin):
    date_hierarchy = "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': ("Author", "Image", "Title", "Content")
        }),
        ('Advanced options', {
            'classes': ('wide', 'collapse', 'extrapretty'),
            'fields': ("Status", "Published_Date", "Category", "Tags"),
        }),
    )
    list_display= ("Title", "Author" ,"Status", "Published_Date")
    list_filter= ("Status", "Author", "Published_Date")
    search_fields= ["Title", "Content"]


admin.site.register(Post, Admin_PostCustomizations)

class Admin_CategoryCustomiztions(admin.ModelAdmin):
    pass

admin.site.register(Category, Admin_CategoryCustomiztions)

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