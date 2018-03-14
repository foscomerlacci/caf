# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0005_auto_20180228_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestazione',
            name='prestazione',
            field=models.CharField(choices=[('730', '730'), ('unico', 'unico'), ('IMU', 'IMU'), ('patronato', 'patronato'), ('consulenza', 'consulenza')], max_length=12),
        ),
    ]
