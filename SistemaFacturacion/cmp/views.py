from os.path import isdir

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from cmp.forms import ProveedorForm

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
        form.instace.usuario_creador = self.request.user
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
