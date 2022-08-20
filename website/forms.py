from django import forms
from website.models import Contact, NewsLetter

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('First_Name', 'Last_Name', 'Email', 'Subject', 'Message')

class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'