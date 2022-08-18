from django import forms
from website.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('First_Name', 'Last_Name', 'Email', 'Subject', 'Message')