from django.urls import path


from .views import CategoriaView,CategoriaCreate,CategoriaEdit,CategoriaBorrar

urlpatterns = [
    path('categoria/', CategoriaView.as_view(),name='categoria_list'),
    path('categoria/nueva',CategoriaCreate.as_view(),name='categoria_nueva'),
    path('categoria/editar/<int:pk>',CategoriaEdit.as_view(),name='categoria_editar'),
    path('categoria/borrar/<int:pk>',CategoriaBorrar.as_view(),name='categoria_borrar')
    
]
