from django import forms
from .models import Students

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'phone', 'email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['phone']