# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0031_auto_20180309_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestazione',
            name='saldo',
            field=models.DecimalField(null=True, decimal_places=2, default=0, max_digits=6),
        ),
    ]
