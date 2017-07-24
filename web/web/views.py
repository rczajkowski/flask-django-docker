from django.http import HttpResponse

from django.shortcuts import render
import requests
import json
from settings import URL_FOR_API_USER
from forms import UserForm


def all_users(request):
    r = requests.get(URL_FOR_API_USER)
    users = r.json()

    users_dict = json.dumps(users)

    return render(request, 'users.html', {'users': json.loads(users_dict)['objects']})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            data_form = form.cleaned_data
            username = data_form['username']
            password = data_form['password']

            data = json.dumps({u'username': username, u'password': password})
            headers = {'content-type': 'application/json'}

            r = requests.post(url=URL_FOR_API_USER, data=data, headers=headers)

            if r.status_code == 201:
                return HttpResponse("success")
    else:
        form = UserForm()

    return render(request, 'add_new.html', {'form': form})
