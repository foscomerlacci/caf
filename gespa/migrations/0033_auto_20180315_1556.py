# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0032_auto_20180313_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='congiunto',
            field=models.CharField(blank=True, max_length=100, default=('sin', 'singolo'), null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='convenzionato',
            field=models.CharField(choices=[('no', 'no'), ('ENI', 'ENI'), ('ERG', 'ERG'), ('APV', 'APVE'), ('alt', 'altro')], max_length=3, default=('no', 'no'), null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='reddito',
            field=models.CharField(choices=[('dip', 'dipendente'), ('pen', 'pensionato')], max_length=3, default=('dip', 'dipendente')),
        ),
    ]
