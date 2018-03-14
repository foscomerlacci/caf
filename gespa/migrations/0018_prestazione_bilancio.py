# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0017_auto_20180228_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestazione',
            name='bilancio',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2),
        ),
    ]
