# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0024_prestazione_saldo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestazione',
            options={'ordering': ['saldo'], 'verbose_name_plural': 'prestazioni'},
        ),
    ]
