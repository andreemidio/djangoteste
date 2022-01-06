from ajax_datatable import AjaxDatatableView
from django.contrib.auth.models import Permission

from django.shortcuts import render

from produtos.models import Products


class ProdutosAjaxDatatableView(AjaxDatatableView):
    model = Products
    title = 'Products'
    initial_order = [["id", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },

    ]

def index(request):
    return render(request, 'index.html', {})
