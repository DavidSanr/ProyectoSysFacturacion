from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView


from .form import CategoriaForm,SubCategoriaForm,MarcaForm,UnidadMedidaForm,ProductoForm
from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto

# Create your views here.

#region Categorias Vistas
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

#endregion

#region SubCategorias Vistas
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

#endregion


#region Marca Vistas 
    
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
    
    marca:Marca = Marca.objects.filter(pk = id ).first()
    contexto={}
    template_name= "inv/catalogos_borrar.html"
    if not marca:
        redirect("inv:marca_list")
        
    if request.method =='GET':
        contexto = {'obj':marca}
    if request.method == 'POST':
        marca.estado = False
        marca.save()
        return redirect("inv:marca_list")
        
    return render(request,template_name,contexto)


#endregion



#region Unidad de medida Vistas

class UnidadMedidaView(LoginRequiredMixin,ListView):
    model = UnidadMedida
    template_name = 'inv/unidadMedida/unidad_medida_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    
    
class UnidadMedidaCreate(LoginRequiredMixin,CreateView):
    model = UnidadMedida
    template_name='inv/unidadMedida/unidad_medida_form.html'
    context_object_name = 'obj'
    form_class = UnidadMedidaForm
    success_url =  reverse_lazy('inv:unidad_medida_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(LoginRequiredMixin, UpdateView):
    model = UnidadMedida
    template_name='inv/unidadMedida/unidad_medida_form.html'
    context_object_name = 'obj'
    form_class = UnidadMedidaForm
    success_url =  reverse_lazy('inv:unidad_medida_list')
    login_url="bases:login"
    def form_valid(self, form):
        form.instance.usuario_modificador = self.request.user.id
        return super().form_valid(form)


def unidad_medida_inactivar(request,id):
    
    unidad_medida:UnidadMedida = UnidadMedida.objects.filter(pk = id ).first()
    contexto={}
    template_name= "inv/catalogos_borrar.html"
    if not unidad_medida:
        redirect("inv:unidad_medida_list")
        
    if request.method =='GET':
        contexto = {'obj':unidad_medida}
    if request.method == 'POST':
        unidad_medida.estado = False
        unidad_medida.save()
        return redirect("inv:unidad_medida_list")
        
    return render(request,template_name,contexto)

#endregion


#region Productos Vista 

class ProductoView(LoginRequiredMixin,ListView):
    model = Producto
    template_name = 'inv/producto/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    
    
class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    template_name='inv/producto/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url =  reverse_lazy('inv:producto_list')
    login_url="bases:login"
    
    
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name='inv/producto/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url =  reverse_lazy('inv:producto_list')
    login_url="bases:login"
    def form_valid(self, form):
        form.instance.usuario_modificador = self.request.user.id
        return super().form_valid(form)


def producto_inactivar(request,id):
    
    # unidad_medida:UnidadMedida = UnidadMedida.objects.filter(pk = id ).first()
    prod = Producto.objects.filter(pk = id).first()
    contexto={}
    template_name= "inv/catalogos_borrar.html"
    if not prod:
        redirect("inv:producto_list")
        
    if request.method =='GET':
        contexto = {'obj':prod}
    if request.method == 'POST':
        prod.estado = False
        prod.save()        
        return redirect("inv:producto_list")
        
    return render(request,template_name,contexto)


#endregion


    
    