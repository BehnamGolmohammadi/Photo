from django.shortcuts import render, redirect
from website.forms import ContactForm
from django.contrib import messages
# Create your views here.
def website_home(request):
    return render(request, 'website/index.html')

def website_about(request):
    return render(request, 'website/about.html')

def website_contact(request):

    if request.method == 'POST':
        Form = ContactForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            messages.success(request, 'Your message has been saved successfully!')
            return redirect('/')
        else:
            msg="Your info or messages are not valid! Do you fill all fields correctly?"
            messages.error(request, msg)
            return redirect('/contact')


    Form = ContactForm()
    return render(request, 'website/contact.html', {'Form': Form})