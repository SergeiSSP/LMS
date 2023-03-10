import datetime

from django.core.validators import MinLengthValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        max_length=250,
        verbose_name='first name',
        db_column='first name',
        validators=[MinLengthValidator(2)],
    )
    last_name = models.CharField(
        max_length=250,
        verbose_name='last name',
        db_column='last name',
        validators=[MinLengthValidator(2)],
        error_messages={
            'min_length': 'Please enter password more than 2 digits.'
        }
    )
    birthday = models.DateField(
        default=datetime.date.today,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
