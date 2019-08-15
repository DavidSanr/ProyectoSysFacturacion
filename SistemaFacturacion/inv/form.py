from django import forms

from .models import Categoria,SubCategoria,Marca


class CategoriaForm (forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripcion de la categoria',
                  "estado": "Estados"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class SubCategoriaForm (forms.ModelForm):

    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'categoria':'Categoria perteneciente','descripcion': 'Sub categoria',
                  "estado": "Estados"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):

        super(SubCategoriaForm,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        
        self.fields['categoria'].empty_label = "Seleccione Categoria"


class MarcaForm (forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Sub categoria',
                    "estado": "Estados"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):

        super(MarcaForm,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        
        