# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0028_remove_prestazione_saldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestazione',
            name='saldo',
            field=models.DecimalField(max_digits=6, decimal_places=2, default=0),
        ),
    ]
