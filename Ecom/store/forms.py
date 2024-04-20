from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class Registerform(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["username","first_name","last_name","email","password"]
class Registerform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"firstname"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"lastname"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password1"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password2"}))
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))

class orderform(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"address","rows":5}))


