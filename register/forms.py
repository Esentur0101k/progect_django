from django import forms
from .models import User
from django.contrib.auth import authenticate



class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'password','username']




class CustomlLoginForm(forms.ModelForm):
    email = forms.EmailField(label='email')
    password = forms.CharField(widget=forms.PasswordInput)



    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')


        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache  is None:
                raise forms.ValidationError('error login')
        return self.cleaned_data
