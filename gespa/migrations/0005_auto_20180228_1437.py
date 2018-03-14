# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0004_auto_20180228_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestazione',
            name='cinquepermille',
            field=models.NullBooleanField(default=False),
        ),
    ]
