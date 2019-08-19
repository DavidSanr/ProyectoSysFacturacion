from django.urls import path


from .views import CategoriaView,CategoriaCreate,CategoriaEdit,CategoriaBorrar,\
SubCategoriaView,SubCategoriaCreate,SubCategoriaEdit,SubCategoriaBorrar, \
    MarcaView,MarcaCreate,MarcaEdit,MarcaBorrar, marca_inactivar, \
    UnidadMedidaView,UnidadMedidaCreate,UnidadMedidaEdit,unidad_medida_inactivar
    
    

urlpatterns = [
    #Categorias
    path('categoria/', CategoriaView.as_view(),name='categoria_list'),
    path('categoria/nueva',CategoriaCreate.as_view(),name='categoria_nueva'),
    path('categoria/editar/<int:pk>',CategoriaEdit.as_view(),name='categoria_editar'),
    path('categoria/borrar/<int:pk>',CategoriaBorrar.as_view(),name='categoria_borrar'),
    #SubCategorias
    path('subcategorias/',SubCategoriaView.as_view(),name='subcategoria_list'),
    path('subcategoria/nueva',SubCategoriaCreate.as_view(),name='subcategoria_nueva'),
    path('subcategoria/editar/<int:pk>',SubCategoriaEdit.as_view(),name='subcategoria_editar'),
    path('subcategoria/borrar/<int:pk>',SubCategoriaBorrar.as_view(),name='subcategoria_borrar'),
    #Marca
    path('marca/',MarcaView.as_view(),name='marca_list'),
    path('marca/nueva',MarcaCreate.as_view(),name='marca_nueva'),
    path('marca/editar/<int:pk>',MarcaEdit.as_view(),name='marca_editar'),
    path('marca/inactivar/<int:id>',marca_inactivar,name='marca_inactivar'),
    #Unidad De medida
    path('unidadmedida/',UnidadMedidaView.as_view(),name='unidad_medida_list'),
    path('unidadmedida/nueva',UnidadMedidaCreate.as_view(),name='unidad_medida_nueva'),
    path('unidadmedida/editar/<int:pk>',UnidadMedidaEdit.as_view(),name='unidad_medida_editar'),
    path('unidadmedida/inactivar/<int:id>',unidad_medida_inactivar,name='unidad_medida_inactivar'),
    
]
