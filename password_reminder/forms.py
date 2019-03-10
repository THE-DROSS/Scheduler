from django import forms


class PasswordReminderForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    new_password = forms.CharField(required=True)
    new_password_confirmed = forms.CharField(required=True)
