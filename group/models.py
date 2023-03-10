import datetime

from django.db import models


class Group(models.Model):
    name_of_group = models.CharField(
        max_length=250,
    )
    date_of_start = models.DateField(
        default=datetime.datetime.today,
        verbose_name='Beginning',
    )
    description = models.TextField()
