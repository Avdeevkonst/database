from django.db import models
from django.urls import reverse


class User(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, default="", verbose_name='Почта')
    paid_user = models.BooleanField(default=False, verbose_name='Платный пользователь')
    time_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Зарегистрированные пользователи'
        verbose_name_plural = 'Зарегистрированные пользователи'
