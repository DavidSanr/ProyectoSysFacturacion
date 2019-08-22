


from django.contrib import admin



from .models import Categoria,SubCategoria,Producto

# Register your models here.




@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass
