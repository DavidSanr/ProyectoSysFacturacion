from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView


from .form import CategoriaForm,SubCategoriaForm,MarcaForm
from .models import Categoria,SubCategoria,Marca

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
    
    
class SubCategoriaEdit(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url =  reverse_lazy('inv:subcategoria_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_modificador = self.request.user.id
        return super().form_valid(form)
    
    
class SubCategoriaBorrar (LoginRequiredMixin,DeleteView):
    model = SubCategoria
    template_name = "inv/subcategoria_borrar.html"
    context_object_name = 'obj'
    success_url =  reverse_lazy('inv:subcategoria_list')
    login_url="bases:login"
    
class MarcaView(LoginRequiredMixin,ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    
    
class MarcaCreate(LoginRequiredMixin,CreateView):
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url =  reverse_lazy('inv:marca_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url =  reverse_lazy('inv:marca_list')
    login_url="bases:login"
    def form_valid(self, form):
        form.instance.usuario_modificador = self.request.user.id
        return super().form_valid(form)
    
class MarcaBorrar (LoginRequiredMixin,DeleteView):
    model = Marca
    template_name = "inv/marca_borrar.html"
    context_object_name = 'obj'
    success_url =  reverse_lazy('inv:marca_list')
    login_url="bases:login"


def marca_inactivar(request,id):
    
    marca = Marca.objects.filter(pk = id ).first()
    contexto={}
    template_name= "inv/catalogos_borrar.html"
    if not marca:
        redirect("inv:marca_list")
        
    if request.method =='GET':
        contexto = {'obj':marca}
        
        
    return render(request,template_name,contexto)
    
    