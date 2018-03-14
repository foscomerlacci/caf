# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0022_auto_20180301_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestazione',
            name='_bilancio',
        ),
    ]
