# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0007_auto_20180228_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='avere',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='dare',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2),
        ),
    ]
