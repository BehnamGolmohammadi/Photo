from django.contrib import admin
from blog.models import Post, Category, Comment


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

class Admin_CommentCustomization(admin.ModelAdmin):
    date_hierarchy= "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': ("Name" ,"Message", "Email")
        }),
        ('Advanced options', {
            'classes': ('wide', 'collapse', 'extrapretty'),
            'fields': ("Post","Approved"),
        }),
    )
    list_display= ("Name", "Post", "Approved", "Created_Date")
    list_filter= ("Approved", "Post")
    search_fields= ["Name", "Message", "Subject"]


admin.site.register(Comment, Admin_CommentCustomization)