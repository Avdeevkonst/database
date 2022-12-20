from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic import ListView, CreateView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin

possibility = [{'title': "Информация о сайте", 'url_name': 'info'},
               {'title': "Загрузить файл", 'url_name': 'addfile'},
               {'title': "Список файлов", 'url_name': 'file'},
               ]


def start(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/index.html', context=context)


class AddFile(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFileForm
    template_name = 'base/addfile.html'
    success_url = reverse_lazy('addfile')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))


# def addfile(request):
#    if request.method == 'POST':
#        form = AddFile(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = AddFile()
#    context = {'form': form, 'title': title,
#               'Add documents': "Загрузить файл",
#               'start_page': "Начальная страница"}
#    return render(request, 'base/addfile.html', context=context)


def info(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/info.html', context=context)


# def registration(request):
#    if request.method == 'POST':
#        form = Authorization(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('base/user.html')
#    else:
#        form = Authorization()
#    context = {'form': form, 'title': title,
#               'Add documents': "Загрузить файл",
#               'start_page': "Начальная страница"}
#    return render(request, 'base/registration.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'base/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'base/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('user')


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def user(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/user.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class FileListView(LoginRequiredMixin, DataMixin, ListView):
    model = File
    success_url = reverse_lazy('file')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))
