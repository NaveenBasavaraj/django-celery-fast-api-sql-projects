from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username' ,'password']
        # excludes = []
        
        label = {
            'password':'Password'
        }
        
        def clean_email(self):
            if self.cleaned_data['email'].endsWith('@gmail.com'):
                return self.cleaned_data['email']
            else:
                raise ValidationError("Invalid Email")
        
        def save(self):
            password = self.cleaned_data.pop('password')
            u = super().save()
            u.set_password(password)
            u.save()
        