from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    password  = forms.CharField(label = 'password', widget = forms.PasswordInput)
    password2  = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields= ['username', 'email', 'first_name', 'last_name']
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email
        