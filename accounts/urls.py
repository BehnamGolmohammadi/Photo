from django.urls import path, include
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', accounts_signup, name = 'signup')
]