from django.urls import path
from .views import ProveedorView,ProveedorNew,ProveedorEdit,proveedor_inactivar

urlpatterns = [    
#Proveedor URL
path('proveedor/',ProveedorView.as_view(), name = 'proveedor_list'),
path('proveedor/nuevo',ProveedorNew.as_view(), name='proveedor_nuevo'),
path('proveedor/editar/<int:pk>',ProveedorEdit.as_view(),name='proveedor_editar'),
path('proveedor/inactivar/<int:pk>',proveedor_inactivar,name='proveedor_inactivar')

]
