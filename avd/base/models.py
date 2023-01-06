from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserInfo(models.Model):
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

    def get_absolute_url(self):
        return reverse('home', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Зарегистрированные пользователи'
        verbose_name_plural = 'Зарегистрированные пользователи'
        ordering = ['first_name', 'second_name', 'email']


class File(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя файла')
    time_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    load_file = models.FileField(upload_to='files/%Y/%m/', verbose_name='Загрузить файл')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Загруженные файлы'
        verbose_name_plural = 'Загруженные файлы'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
