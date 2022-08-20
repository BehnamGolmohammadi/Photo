from django.urls import path, include
from accounts.views import *
from django.contrib.auth import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login', accounts_login, name= 'login'),
    path('logout', accounts_logout, name= 'logout'),
    path('signup', accounts_signup, name = 'signup')
]