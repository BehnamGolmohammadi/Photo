from django.urls import path
from blog.views import *

app_name= 'blog'

urlpatterns = [
    path('', blog_home, name='home'),
    path('category/<str:cat>', blog_home, name='category'),
    path('<int:pid>', blog_post, name='post'),
]