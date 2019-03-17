from django import forms
from django.core.exceptions import ValidationError


class PasswordReminderForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    new_password = forms.CharField(required=True, min_length=8, max_length=16)
    new_password_confirmed = forms.CharField(required=True, min_length=8, max_length=16)

    def clean_new_password(self):
        new_password = self.cleaned_data['new_password']
        # TODO 英数記チェック
        return new_password

    def clean(self):
        cleaned_data = self.cleaned_data
        new_password = cleaned_data.get('new_password')
        new_password_confirmed = cleaned_data.get('new_password_confirmed')
        if not new_password == new_password_confirmed:
            raise forms.ValidationError(u'パスワードが異なります。')
        return cleaned_data
