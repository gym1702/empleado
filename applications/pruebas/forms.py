from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese titulo',
                    'class': 'text',
                }
            )
        }


    #VALIDA QUE LA CANTIDAD SEA MAYOR A 10
    def clean_cantidad(self):
        cant = self.cleaned_data['cantidad']
        if cant < 10:
            raise forms.ValidationError('El valor indicado debe ser mayor a 10')
        return cant



      