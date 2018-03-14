# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0029_prestazione_saldo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestazione',
            options={'verbose_name_plural': 'id'},
        ),
    ]
