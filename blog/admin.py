from django.contrib import admin
from blog.models import Post


# Register your models here.
class Admin_PostCustomizations(admin.ModelAdmin):
    date_hierarchy = "Created_Date"


admin.site.register(Post)