# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0014_auto_20180228_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='avere',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='dare',
            field=models.FloatField(default=0),
        ),
    ]
