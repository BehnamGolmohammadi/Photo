from django.shortcuts import render, redirect, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
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

def website_newsletter(request):
    if request.method == 'POST':
        Form= NewsletterForm(request.POST)
        if Form.is_valid:
            try:
                Form.save()
                messages.success(request, 'Well done.\nYou will recive newsletter every days since now.')
            except:
                messages.warning(request, 'Your email format is not valid\nPlease try agian.')
                return HttpResponseRedirect('/#newsletter')
        else:
            print(request.POST)
            messages.error(request, 'Your input is not like an E-mail\nPlease try agian.')
    Form= NewsletterForm
    return HttpResponseRedirect('/')

