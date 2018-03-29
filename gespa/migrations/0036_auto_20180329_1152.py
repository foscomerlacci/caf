# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0035_auto_20180329_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='prima_casa',
            field=models.BooleanField(),
        ),
    ]
