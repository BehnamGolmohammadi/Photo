from django.urls import path
from website.views import *

app_name= 'website'

urlpatterns = [
    path('', website_home, name='home'),
    path('about', website_about, name='about'),
    path('contact', website_contact, name='contact'),
]