from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import widgets

User = get_user_model()


class createUserForm(UserCreationForm):
       
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Email Address"
    }))
    first_name= forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "First Name",
        "autocomplete":"username"
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Last Name",
        "autocomplete":"username"
    }))

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
        
        
    def __init__(self, *args, **kwargs):
        super(createUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username', "autocomplete":"username"})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter password', 'autocomplete':"current-password", 'required':"", 'id': "id_password1"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Confirm password', 'autocomplete':"current-password", 'required':"", 'id': "id_password2"})
        
    
        


    

    