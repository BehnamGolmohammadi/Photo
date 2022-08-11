from django.urls import path
from blog.views import *

app_name= 'blog'

urlpatterns = [
    path('', blog_home, name='home'),
    path('post', blog_post, name='post'),
]