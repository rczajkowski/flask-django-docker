from django.http import HttpResponse
from django.shortcuts import render
from forms import UserForm
from user import User


def show_all_users(request):
    user = User(None, None)

    return render(request, 'users.html', {'users': user.get_all_users()})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            request = form.save()

            if request.status_code == 201:
                return HttpResponse("success")
    else:
        form = UserForm()

    return render(request, 'add_new.html', {'form': form})
