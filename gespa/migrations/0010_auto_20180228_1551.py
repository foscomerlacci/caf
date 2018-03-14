# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0009_auto_20180228_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestazione',
            name='prestazione',
            field=models.IntegerField(choices=[(1, '730'), (2, 'unico'), (3, 'IMU'), (4, 'patronato'), (5, 'consulenza')], max_length=1),
        ),
    ]
