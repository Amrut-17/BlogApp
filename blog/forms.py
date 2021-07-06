from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import BlogPost
class SignUp(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class':'form-control'
            }), label='Confirm Password ')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class':'form-control'
            }), label='Password ')
            
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
        labels ={
            'first_name':'First Name ',
            'username':'UserName ',
            'email':'Email ',
        }
        widgets ={
            'username':forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Username'
            }),

            'first_name':forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'First Name'
            }),

            'email':forms.EmailInput(attrs={
                'class':'form-control', 'placeholder':'name@example.com'
            })
        }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'aitofocus':True,
        'class':'form-control',
    }))

    password = forms.CharField(label=_("Password"), strip=False,
    widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password',
        'class':'form-control',
    }))

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'desc']
        labels = {
            'title':'Post Title',
            'desc' : 'Post'
        }
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'desc':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),
        }