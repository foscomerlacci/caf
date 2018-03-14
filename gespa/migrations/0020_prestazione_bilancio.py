# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0019_remove_prestazione_bilancio'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestazione',
            name='bilancio',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=6),
        ),
    ]
