# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0023_remove_prestazione__bilancio'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestazione',
            name='saldo',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=6),
        ),
    ]
