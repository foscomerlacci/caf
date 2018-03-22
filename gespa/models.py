from django.db import models
from italian_utils.validators import validate_codice_fiscale
from django.utils import timezone
from django.db import connection
from django.db.models import signals
# from .admin import PrestazioneAdmin



# Create your models here.

class Cliente(models.Model):
    scelte_stato = (
        ('sin', 'singolo'),
        ('con','congiunto'),
        )
    scelte_reddito = (
        ('dip', 'dipendente'),
        ('pen', 'pensionato'),
        )
    scelte_convenzionato = (
        ('no', 'no'),
        ('ENI', 'ENI'),
        ('ERG','ERG'),
        ('APV','APVE'),
        ('alt','altro'),
        )
    scelte_prima_casa = (
        ('no', 'No'),
        ('si', 'Si'),
    )
    scelte_seconda_casa = (
        ('no', 'No'),
        ('si', 'Si'),
    )
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    cf = models.CharField(verbose_name='Codice fiscale', max_length=16, validators=[validate_codice_fiscale])
    tel_fisso = models.CharField(max_length=12, null=True, blank=True)
    tel_cellulare = models.CharField(max_length=12, null=True, blank=True)
    prima_casa = models.NullBooleanField(default=False)
    seconda_casa = models.NullBooleanField(default=False)
    stato = models.CharField(max_length=3, choices=scelte_stato, default=scelte_stato[0])
    congiunto = models.CharField(max_length=100, null=True, blank=True)
    reddito = models.CharField(max_length=3, choices=scelte_reddito, default=scelte_reddito[0])
    convenzionato = models.CharField(max_length=3, choices=scelte_convenzionato, null=True, default=scelte_convenzionato[0] )

    def __str__(self):
        # return self.cf
        return str(self.nome).capitalize() + " " + str(self.cognome).capitalize()

    class Meta:
        verbose_name_plural = 'clienti'


class Prestazione(models.Model):
    scelte_prestazione = (
        ('730', '730'),
        ('unico', 'unico'),
        ('IMU', 'IMU'),
        ('patronato', 'patronato'),
        ('consulenza', 'consulenza'),
        )
    prestazione = models.CharField(max_length=10, choices=scelte_prestazione)
    cinquepermille = models.NullBooleanField(default= False)
    cliente = models.ForeignKey('Cliente')
    data = models.DateTimeField(auto_now_add= False, default=timezone.now)
    saldo = models.DecimalField(max_digits=6, decimal_places=2, default=0, null= True)
    note = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        # return self.prestazione.__str__()
        # return self.id.__str__()
        return self.prestazione.__str__() + " su cliente " + str(self.cliente.nome).capitalize() + " " + str(self.cliente.cognome).capitalize()

    class Meta:
        verbose_name_plural = 'prestazioni'


## questa è la chiamata raw alla query che aggiorna il saldo della prestazione
## legata all'ultimo pagamento inserito

def agg_saldo(sender, instance, created, **kwargs ):
    cursor = connection.cursor()
    listaIndici = []
    cursor.execute('''SELECT gespa_prestazione.id FROM gespa_prestazione ORDER BY gespa_prestazione.id''')
    rows = cursor.fetchall()

    for element in rows:
        listaIndici.append(element[0])



    for x in listaIndici:
        y = z = x
        cursor = connection.cursor()
        cursor.execute('''UPDATE gespa_prestazione\
                      SET saldo = (SELECT(SUM(gespa_pagamento.dare) - SUM(gespa_pagamento.avere))\
                                  FROM gespa_pagamento JOIN gespa_prestazione ON gespa_prestazione.id = gespa_pagamento.prestazione_id\
                                  WHERE gespa_prestazione.id = ?)
                      WHERE gespa_prestazione.id = ?''', (y, z))
    # cursor.execute('''UPDATE gespa_prestazione\
    #                   SET saldo = (SELECT(SUM(gespa_pagamento.dare) - SUM(gespa_pagamento.avere))\
    #                               FROM gespa_pagamento JOIN gespa_prestazione ON gespa_prestazione.id = gespa_pagamento.prestazione_id\
    #                               WHERE gespa_prestazione.id = (SELECT gespa_pagamento.prestazione_id\
    #                                                             FROM gespa_pagamento\
    #                                                             ORDER BY gespa_pagamento.id\
    #                                                             DESC LIMIT -1)\
    #                               )\
    #                   WHERE gespa_prestazione.id = (\
    #                                                 SELECT gespa_prestazione.id\
    #                                                 FROM gespa_prestazione\
    #                                                 JOIN gespa_pagamento ON gespa_prestazione.id = gespa_pagamento.prestazione_id\
    #                                                 ORDER BY gespa_pagamento.id\
    #                                                 DESC LIMIT -1)''')


class Pagamento(models.Model):
    data = models.DateTimeField(auto_now_add=False, default=timezone.now)
    prestazione = models.ForeignKey('Prestazione')
    dare = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    avere = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        # return self.prestazione.prestazione
        return self.prestazione.cliente.cf

    def cliente(self):
        nome = self.prestazione.cliente.nome
        cognome = self.prestazione.cliente.cognome
        return nome + " " + cognome

    class Meta:
        verbose_name_plural = 'pagamenti'

# richiamo la funzione agg_saldo dopo il salvataggio di un pagamento
signals.post_save.connect(agg_saldo, sender = Pagamento)