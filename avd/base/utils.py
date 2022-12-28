from .models import *

title = 'AvdBASE'

possibility = [{'title': "Информация о сайте", 'url_name': 'info'},
               {'title': "Загрузить файл", 'url_name': 'addfile'},
               {'title': "Список файлов", 'url_name': 'file'},
               ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        files = UserInfo.objects.all()
        context['files'] = files
        context['title'] = title
        context['possibility'] = possibility
        return context
