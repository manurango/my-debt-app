# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-16 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='debt_statu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('customer_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('original_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('intrest_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('present_balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
