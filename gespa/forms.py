from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'nome',
            'cognome',
            'cf',
            'tel_fisso',
            'tel_cellulare',
            'reddito',
            'prima_casa',
            'seconda_casa',
            'stato',
            'congiunto',
            'convenzionato',)

## configuro i widgets per poter disporre dei valori da confrontare nei javascript

        widgets = {
            'prima_casa': forms.Select(choices=Cliente.scelte_prima_casa),
            'seconda_casa': forms.Select(choices=Cliente.scelte_seconda_casa),
            'stato': forms.Select(choices=Cliente.scelte_stato),
        }

## importo i javascript per jquery in modo da rendere dinamici i campi 'seconda_casa' e 'congiunto'

    class Media:
        js = (
            '/static/seconda_casa.js',
            '/static/congiunto.js',
        )

