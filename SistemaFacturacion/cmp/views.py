from os.path import isdir

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import ProveedorForm
from .models import Proveedor

# Create your views here.

class ProveedorView(LoginRequiredMixin,ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name="obj"
    login_url = "base:login"
    
    
class ProveedorNew(LoginRequiredMixin,CreateView):
    model= Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'
    
    def form_valid(self,form):
        form.instance.usuario_creador = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)
    
    
class ProveedorEdit(LoginRequiredMixin,UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'
    
    
    def form_valid(self,form):
        form.instance.usuario_modificador= self.request.user.dir
        print(self.request.user.id)
        return super().form_valid(form)
    
def proveedor_inactivar(request,id):    
    # unidad_medida:UnidadMedida = UnidadMedida.objects.filter(pk = id ).first()
    prove = Proveedor.objects.filter(pk = id).first()
    contexto={}
    template_name= "cmp/cmp_borrar.html"
    if not prove:
        return HttpResponse('Proveedor No existe' + str(id))
        
        
    if request.method =='GET':
        contexto = {'obj':prove}
    if request.method == 'POST':
        prove.estado = False
        prove.save()        
        return redirect("cmp:proveedor_list")
        
    return render(request,template_name,contexto)
