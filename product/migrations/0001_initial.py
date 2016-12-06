# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255, choices=[(b'electronics', b'electronics'), (b'fashion', b'fashion')])),
                ('photo', models.FileField(upload_to=b'uploads/%Y/%m/%d')),
                ('descrip', models.TextField(max_length=1200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
