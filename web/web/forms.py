from django import forms
from user import User


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def save(self):
        data_form = self.cleaned_data
        username = data_form['username']
        password = data_form['password']

        user = User(username, password)

        request = user.save_user()

        return request