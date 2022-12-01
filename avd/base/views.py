from datetime import *
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
title = 'AvdBASE'
possibility = [
    {'title': "Регистрация", 'url_name': 'registration'},
    {'title': "Вход", 'url_name': 'login'},
    {'title': "Информация о сайте", 'url_name': 'info'},
    {'title': "Обратная связь", 'url_name': 'feedback'}
]


def start(request):
    context = {'possibility': possibility,
               'title': title}
    return render(request, 'base/index.html', context=context)


def archive(request, year):
    now = datetime.now()
    now_year = now.year
    if int(year) > now_year:
        return redirect('/')
    return HttpResponse(f"<h1>Архив данных по годам</h1><p>{year}</p>")


def info(request):
    context = {'possibility': possibility,
               'title': title}
    return render(request, 'base/info.html', context=context)


def registration(request):
    return render(request, 'base/registration.html')


def login(request):
    return render(request, 'base/login.html')


def feedback(request):
    return render(request, 'base/feedback.html')


def user_account(request):
    return render(request, 'base/user_account.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
