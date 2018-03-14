# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0015_auto_20180228_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='avere',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='dare',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=6),
        ),
    ]
