# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0002_auto_20180223_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'clienti'},
        ),
        migrations.AlterModelOptions(
            name='pagamento',
            options={'verbose_name_plural': 'pagamenti'},
        ),
        migrations.AlterModelOptions(
            name='prestazione',
            options={'verbose_name_plural': 'prestazioni'},
        ),
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
