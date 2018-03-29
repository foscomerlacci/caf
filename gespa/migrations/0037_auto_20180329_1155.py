# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0036_auto_20180329_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='prima_casa',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='seconda_casa',
            field=models.NullBooleanField(default=False),
        ),
    ]
