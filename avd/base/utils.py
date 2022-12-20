from .models import *

title = 'AvdBASE'

possibility = [{'title': "Информация о сайте", 'url_name': 'info'},
               {'title': "Загрузить файл", 'url_name': 'addfile'},
               {'title': "Список файлов", 'url_name': 'file'},
               ]


class DataMixin:
    def __init__(self):
        self.request = None

    def get_user_context(self, **kwargs):
        context = kwargs
        files = File.objects.all()
        context['files'] = files
        context['title'] = title
        context['possibility'] = possibility
        return context
