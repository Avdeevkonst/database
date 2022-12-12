from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic import ListView

title = 'AvdBASE'
possibility = [{'title': "Регистрация", 'url_name': 'registration'},
               {'title': "Вход", 'url_name': 'login'},
               {'title': "Информация о сайте", 'url_name': 'info'},
               {'title': "Загрузить файл", 'url_name': 'addfile'}, ]


def start(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/index.html', context=context)


def addfile(request):
    if request.method == 'POST':
        form = AddFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddFile()
    context = {'form': form, 'title': title,
               'Add documents': "Загрузить файл",
               'start_page': "Начальная страница"}
    return render(request, 'base/addfile.html', context=context)


def info(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/info.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = Authorization(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base/user.html')
    else:
        form = Authorization()
    context = {'form': form, 'title': title,
               'Add documents': "Загрузить файл",
               'start_page': "Начальная страница"}
    return render(request, 'base/registration.html', context=context)


def login(request):
    return render(request, 'base/login.html')


def user(request):
    return render(request, 'base/user.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# class DataMixin:
# pass


# class RegisterUser(DataMixin, CreateView):
# form_class = UserCreationForm
# template_name = 'base/registration.html'
# success_url = reverse_lazy('login')

# def get_context_data(self, *,  object_list=None, **kwargs):
# context = super().get_context_data(**kwargs)
# c_def = self.get_user_context(title='Регистрация')
# return dict(list(context.items()) + list(c_def.items()))
