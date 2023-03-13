import datetime
from faker import Faker

from django.core.validators import MinLengthValidator
from django.db import models

from .validators import ValidEmailDomain

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com')


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
    email = models.EmailField(
        null=True,
        validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)],
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for i in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            st = cls(first_name=first_name, last_name=last_name, email=email, birthday=birthday)
            try:
                st.full_clean()
                st.save()
            except:
                print(f'Incorrect data - {first_name}{last_name}{email}, {birthday}')
                print(type(first_name))
