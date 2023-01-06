from django.contrib import admin

from .models import *


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name',
                    'email', 'paid_user')
    list_display_links = ('id', 'email', 'paid_user')
    search_fields = ('first_name', 'second_name', 'email')
    list_filter = ('paid_user', 'first_name', 'second_name', 'email')
    prepopulated_fields = {'slug': ("second_name",)}


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_load', 'load_file')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name', 'load_file')


admin.site.register(UserInfo, BaseAdmin)
admin.site.register(File, FileAdmin)

admin.site.site_title = 'Админ-панель AvdBASE'
admin.site.site_header = 'Админ-панель AvdBASE'
