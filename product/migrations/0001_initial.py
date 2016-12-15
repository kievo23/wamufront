# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('photo', models.FileField(upload_to=b'uploads/%Y/%m/%d')),
                ('descrip', models.TextField(max_length=1200)),
                ('wamuprice', models.CharField(max_length=255, null=True)),
                ('book_amount', models.CharField(max_length=255, null=True)),
                ('barcode', models.CharField(max_length=255, null=True)),
                ('visible', models.CharField(max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, to='category.Category', null=True)),
                ('source', models.ForeignKey(blank=True, to='supermarket.Supermarket', null=True)),
            ],
        ),
    ]
