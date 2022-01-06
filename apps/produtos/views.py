from ajax_datatable import AjaxDatatableView
from django.shortcuts import render

from apps.produtos.models import Products


class ProdutosAjaxDatatableView(AjaxDatatableView):
    model = Products
    title = 'Products'
    initial_order = [["id", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'foreign_field': 'id', 'visible': True, },
        {'name': 'consult_date', 'foreign_field': 'consult_date', 'visible': True, },
        {'name': 'product_url_created_at', 'foreign_field': 'product_url_created_at', 'visible': True, },
        {'name': 'product_url_image', 'foreign_field': 'product_url_image', 'visible': True, },
        {'name': 'store_url', 'foreign_field': 'store_url', 'visible': True, },
        {'name': 'c', 'foreign_field': 'c', 'visible': True, },

    ]

def index(request):
    return render(request, 'index.html', {})
