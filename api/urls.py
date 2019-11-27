from django.urls import path
from api.apiviews import ProductoList, CategoriaSave, SubCategoriaSave, ProductoDetalle
 
urlpatterns = [
    path('v1/productos/', ProductoList.as_view(),name='producto_list' ),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),
    path('v1/categorias/', CategoriaSave.as_view(),name='categoria_save' ),
    path('v1/subcategorias/', SubCategoriaSave.as_view(),name='subcategoria_save' ),
]