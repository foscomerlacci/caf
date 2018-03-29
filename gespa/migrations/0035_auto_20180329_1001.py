# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0034_auto_20180315_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='prima_casa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='seconda_casa',
            field=models.BooleanField(default=False),
        ),
    ]
