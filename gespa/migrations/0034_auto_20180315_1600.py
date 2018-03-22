# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0033_auto_20180315_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='congiunto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='stato',
            field=models.CharField(choices=[('sin', 'singolo'), ('con', 'congiunto')], max_length=3, default=('sin', 'singolo')),
        ),
    ]
