from datetime import *
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def start(request):
    return HttpResponse("<h1>Начальная страница сайта.</h1>")


def info(request, info_s):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Информационная страница сайта.</h1><p>{info_s}</p>")


def archive(request, year):
    now = datetime.now()
    now_year = now.year
    if int(year) > now_year:
        return redirect('/')
    return HttpResponse(f"<h1>Архив данных по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
