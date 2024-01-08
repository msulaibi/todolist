from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomRegistrerForm(UserCreationForm):
    email = forms.EmailField()
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already existssss")
        return email # Now form.is_valid() will throw error if an user account with given email already exists.
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name', 'password1', 'password2']
        
    