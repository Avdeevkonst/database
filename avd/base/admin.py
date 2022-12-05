from django.contrib import admin

from .models import *


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name',
                    'email', 'paid_user')
    list_display_links = ('id', 'email', 'paid_user')
    search_fields = ('first_name', 'second_name', 'email')
    list_filter = ('paid_user', 'first_name', 'second_name', 'email')
    prepopulated_fields = {'slug': ("second_name",)}


admin.site.register(User, BaseAdmin)
