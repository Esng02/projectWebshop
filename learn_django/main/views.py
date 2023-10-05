from django.shortcuts import render
from .models import Users
from .forms import UsersForm


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['123', 456, 'jkl']
    }
    return render(request, 'main/index.html', data)


def registration(request):
    link = 'main/registration.html'
    mess = ""
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            mess = "Регистрация прошла успешно"
            link = 'main/sign_in.html'
        else:
            mess = "Неправильно заполнено"

    form = UsersForm()
    data = {
        'form': form,
        'mess': mess,
        'link': link
    }

    return render(request, data['link'], data)


def sign_in(request):
    return render(request, 'main/sign_in.html')
