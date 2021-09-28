# Generated by Django 3.2.6 on 2021-09-23 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('billing_email', models.EmailField(max_length=225)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address_one', models.CharField(blank=True, max_length=225)),
                ('address_two', models.CharField(blank=True, max_length=225)),
                ('city', models.CharField(blank=True, max_length=225)),
                ('country', models.CharField(blank=True, max_length=225)),
                ('postal_code', models.CharField(blank=True, max_length=225)),
            ],
        ),
    ]
