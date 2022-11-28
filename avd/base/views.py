from datetime import *
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
title = 'AvdBASE'
possibility = {"Регистрация", "Вход", "Информация о сайте", "Обратная связь"}


def start(request):
    return render(request, 'base/index.html', {'possibility': possibility, 'title': title})


def info(request):
    return render(request, 'base/info.html', {'possibility': possibility, 'title': title})


def archive(request, year):
    now = datetime.now()
    now_year = now.year
    if int(year) > now_year:
        return redirect('/')
    return HttpResponse(f"<h1>Архив данных по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
