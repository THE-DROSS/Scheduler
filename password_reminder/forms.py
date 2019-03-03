from django import forms


class PasswordReminderForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
