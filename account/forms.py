from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(forms.Form):
    Username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
