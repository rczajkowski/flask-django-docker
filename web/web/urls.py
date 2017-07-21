"""microservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

from django.shortcuts import render
import requests
import json


def all_users(request):
    url = 'http://microservice:8000/api/user'
    r = requests.get(url)
    users = r.json()

    users_dict = json.dumps(users)

    return render(request, 'users.html', {'users': json.loads(users_dict)['objects']})


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        url = 'http://microservice:8000/api/user'
        data = json.dumps({u'username': username, u'password': password})

        headers = {'content-type': 'application/json'}
        r = requests.post(url=url, data=data, headers=headers)
        if r.status_code == 201:
            return HttpResponse("success")

    return render(request, 'add_new.html')


urlpatterns = [
    url(r'^users/', all_users, name='users'),
    url(r'^add', add_user, name='add'),
    url(r'^admin/', admin.site.urls),
]
