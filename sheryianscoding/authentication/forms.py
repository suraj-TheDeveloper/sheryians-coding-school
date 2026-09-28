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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'phone', 'email', 'dob', 'bio', 'pincode', 'city', 'state', 'country']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob': 'Date Of Birth'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone': forms.TelInput(attrs={'placeholder': 'Phone no', 'type': 'tel'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'type': 'email'}),
            'dob': forms.DateInput(attrs={'placeholder': 'Date of birth', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Tell us litte more about you', 'rows': 4}),
            'pincode': forms.NumberInput(attrs={'placeholder': 'Pincode', 'type': 'number'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'})
        }