# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0020_prestazione_bilancio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestazione',
            name='bilancio',
        ),
        migrations.AddField(
            model_name='prestazione',
            name='_bilancio',
            field=models.DecimalField(decimal_places=2, max_digits=6, db_column='bilancio', default=0),
        ),
    ]
