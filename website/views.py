from django.shortcuts import render

# Create your views here.
def website_home(request):
    return render(request, 'test.html')