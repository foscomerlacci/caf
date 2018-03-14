# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import italian_utils.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('cf', models.CharField(max_length=16, validators=[italian_utils.validators.validate_codice_fiscale])),
                ('tel_fisso', models.CharField(max_length=12)),
                ('tel_cellulare', models.CharField(max_length=12)),
                ('congiunto', models.CharField(max_length=100)),
                ('prima_casa', models.NullBooleanField()),
                ('seconda_casa', models.NullBooleanField()),
                ('stato', models.CharField(choices=[('sin', 'singolo'), ('con', 'congiunto')], max_length=3)),
                ('reddito', models.CharField(choices=[('dip', 'dipendente'), ('pen', 'pensionato')], max_length=3)),
                ('convenzionato', models.CharField(choices=[('ENI', 'ENI'), ('ERG', 'ERG'), ('APV', 'APVE'), ('alt', 'altro')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('dare', models.DecimalField(max_digits=6, decimal_places=2)),
                ('avere', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Prestazione',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('prestazione', models.CharField(choices=[('730', '730'), ('uni', 'unico'), ('IMU', 'IMU'), ('pat', 'patronato'), ('con', 'consulenza')], max_length=3)),
                ('cinquepermille', models.NullBooleanField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.TextField(max_length=500)),
                ('cliente', models.ForeignKey(to='gespa.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='pagamento',
            name='prestazione',
            field=models.ForeignKey(to='gespa.Prestazione'),
        ),
    ]
