# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20161127_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='source',
            field=models.ForeignKey(blank=True, to='supermarket.Supermarket', null=True),
        ),
    ]
