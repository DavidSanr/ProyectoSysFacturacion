


from django.contrib import admin



from .models import Categoria,SubCategoria

# Register your models here.




@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    pass