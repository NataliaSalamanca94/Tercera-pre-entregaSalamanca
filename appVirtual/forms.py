from django import forms
from .models import Cliente, Articulo, Tienda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Specify the model for the form
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'