from django import forms


class UserRegisterForm(forms.Form):
    id = forms.CharField()
    pass_hash = forms.CharField()
    email_address = forms.EmailField()
