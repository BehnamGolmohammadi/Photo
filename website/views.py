from django.shortcuts import render

# Create your views here.
def website_home(request):
    return render(request, 'website/index.html')

def website_about(request):
    return render(request, 'website/about.html')

def website_contact(request):
    return render(request, 'website/contact.html')