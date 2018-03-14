# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0030_auto_20180309_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestazione',
            options={'verbose_name_plural': 'prestazioni'},
        ),
    ]
