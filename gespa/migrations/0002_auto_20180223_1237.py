# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gespa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='congiunto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='convenzionato',
            field=models.CharField(choices=[('ENI', 'ENI'), ('ERG', 'ERG'), ('APV', 'APVE'), ('alt', 'altro')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tel_cellulare',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tel_fisso',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='avere',
            field=models.DecimalField(blank=True, max_digits=6, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='dare',
            field=models.DecimalField(blank=True, max_digits=6, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='prestazione',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
