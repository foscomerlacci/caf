# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0027_prestazione_saldo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestazione',
            name='saldo',
        ),
    ]
