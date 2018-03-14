# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import italian_utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0003_auto_20180227_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cf',
            field=models.CharField(max_length=16, verbose_name='Codice fiscale', validators=[italian_utils.validators.validate_codice_fiscale]),
        ),
        migrations.AlterField(
            model_name='prestazione',
            name='prestazione',
            field=models.CharField(max_length=3, choices=[('730', '730'), ('unico', 'unico'), ('IMU', 'IMU'), ('patronato', 'patronato'), ('consulenza', 'consulenza')]),
        ),
    ]
