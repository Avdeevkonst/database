from django.db import models
from django.urls import reverse
from django.core import validators


class User(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, verbose_name='Почта')
    paid_user = models.BooleanField(default=False, verbose_name='Платный пользователь')
    time_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    file = models.ForeignKey('File', on_delete=models.DO_NOTHING, verbose_name="Файл",
                             default='', null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Зарегистрированные пользователи'
        verbose_name_plural = 'Зарегистрированные пользователи'


class File(models.Model):
    name = models.CharField(max_length=30)
    time_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    load_file = models.FileField(verbose_name='Загрузить файл')

    def __str__(self):
        return self.name
