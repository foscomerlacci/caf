# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0012_auto_20180228_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='avere',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='dare',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
