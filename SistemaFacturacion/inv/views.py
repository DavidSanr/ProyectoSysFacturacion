from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView


from .form import CategoriaForm,SubCategoriaForm
from .models import Categoria,SubCategoria

# Create your views here.


class CategoriaView(LoginRequiredMixin,ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    

class CategoriaCreate(LoginRequiredMixin,CreateView):
    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url =  reverse_lazy('inv:categoria_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)
    
class CategoriaEdit(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url =  reverse_lazy('inv:categoria_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_modificador = self.request.user.id
        return super().form_valid(form)
    

class CategoriaBorrar (LoginRequiredMixin,DeleteView):
    model = Categoria
    template_name = "inv/categoria_borrar.html"
    context_object_name = 'obj'
    success_url =  reverse_lazy('inv:categoria_list')
    login_url="bases:login"


class SubCategoriaView(LoginRequiredMixin,ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class SubCategoriaCreate(LoginRequiredMixin,CreateView):
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url =  reverse_lazy('inv:subcategoria_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)
    