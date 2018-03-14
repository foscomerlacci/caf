# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0025_auto_20180302_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestazione',
            options={'verbose_name_plural': 'prestazioni'},
        ),
        migrations.RemoveField(
            model_name='prestazione',
            name='saldo',
        ),
    ]
