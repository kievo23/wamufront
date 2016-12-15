# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1200)),
                ('email', models.EmailField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('yourlogo', models.CharField(max_length=255)),
                ('till_no', models.CharField(max_length=255)),
                ('product_counter', models.CharField(max_length=255)),
                ('receipt_counter', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('receipt_code', models.CharField(max_length=255)),
                ('interest_rate', models.CharField(max_length=255)),
                ('timestamp', models.DateField()),
            ],
        ),
    ]
