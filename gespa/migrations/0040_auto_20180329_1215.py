# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0039_auto_20180329_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='seconda_casa',
            field=models.BooleanField(default=False),
        ),
    ]
