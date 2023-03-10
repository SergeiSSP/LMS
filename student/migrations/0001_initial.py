# Generated by Django 4.1.7 on 2023-03-10 16:29

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first name', max_length=250, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='first name')),
                ('last_name', models.CharField(db_column='last name', error_messages={'min_length': 'Please enter password more than 2 digits.'}, max_length=250, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last name')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]
