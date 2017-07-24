from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', widget=forms.PasswordInput)