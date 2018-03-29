from django.contrib import admin
from django.conf.urls import url
from .forms import ClienteForm
from .models import Pagamento, Cliente, Prestazione
from .toolbox import export_xls




# Register your models here.


class PagamentoInLine(admin.TabularInline):
    model = Pagamento
    extra = 0
    fields = ['data', 'dare', 'avere']
    readonly_fields = ['data',]


class PrestazioneInLine(admin.TabularInline):
    model = Prestazione
    extra = 0
    fields = ['data', 'cinquepermille',]
    readonly_fields = ['data', 'cinquepermille']


class ClienteAdmin(admin.ModelAdmin):

## funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(ClienteAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
##############################################################################
    list_display = ['cf','nome','cognome','convenzionato', 'prima_casa', 'seconda_casa']
    search_fields = ['cf', 'cognome']
    actions = [export_xls]
    form = ClienteForm



class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['data', 'cliente', 'prestazione', 'dare', 'avere']
    actions = None



class PrestazioneAdmin(admin.ModelAdmin):
    list_display = ['id', 'prestazione','cliente', 'data', 'saldo', 'note']
    inlines = [PagamentoInLine]
    actions = None
    # date_hierarchy = 'data'
    list_filter = ('data', 'prestazione')
    readonly_fields = ('saldo',)
    search_fields = ['cliente__cf', 'cliente__nome', 'cliente__cognome']
    save_on_top = True

### funzione per il saldo "on fly" sulla view (funzionanate) #####

    # def saldo(self, obj):
    #     a = obj.pagamento_set.values('avere')
    #     d = obj.pagamento_set.values('dare')
    #     dare = 0
    #     avere = 0
    #
    #     for diz in d:
    #         dare = dare + float(diz['dare'])
    #
    #     for diz in a:
    #         avere = avere + float(diz['avere'])
    #
    #     return dare - avere

##################################################################

admin.site.register(Prestazione, PrestazioneAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site_url = None
# admin.site.register(Pagamento, PagamentoAdmin)
# admin_site = MyAdminSite()
admin.site.site_header = ('CAF di Dono')
admin.site.site_title = ('CAF di Dono')
admin.site.index_title = ('Servizi')

