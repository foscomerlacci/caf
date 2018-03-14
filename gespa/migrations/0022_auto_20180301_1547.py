# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0021_auto_20180301_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestazione',
            name='_bilancio',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2, db_column=0),
        ),
    ]
