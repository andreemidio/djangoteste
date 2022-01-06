from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from produtos.views import ProdutosAjaxDatatableView, index

urlpatterns = [
                  path('', index),
                  path('produtos', ProdutosAjaxDatatableView.as_view(), name="ajax_datatable_permissions"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
