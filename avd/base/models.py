from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=30)
    time_registration = models.DateTimeField(auto_now_add=True)

    #    password =
    def __str__(self):
        return self.first_name
