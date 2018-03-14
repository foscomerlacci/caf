from django.http import HttpResponse
from xlwt.compat import xrange


###  funzione per l'export in xls

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ListaClienti.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("ListaClienti")

    row_num = 0

    columns = [
        (u"cf", 7000),
        (u"Nome", 7000),
        (u"Cognome", 7000),
        (u"Cellulare", 7000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.cf,
            obj.nome,
            obj.cognome,
            obj.tel_cellulare,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Export XLS"