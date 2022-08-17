from django import forms
from website.models import Contact
class ContactForm(forms.ModelForm):

    class META:
        model = Contact
        fields = ['Name', 'Email', 'Subject', 'Message']