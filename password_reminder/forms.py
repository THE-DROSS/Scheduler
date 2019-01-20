from django import forms


class PasswordReminderForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()