from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('first_name', 'last_name', 'job', 'department', 'habilidades', 'hoja_vida', 'image')

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
            self.fields['habilidades'].widget.attrs.update({
                'class': ''
            })
        
        # self.fields['habilidades'].widget.attrs['CheckboxSelectMultiple'] = True

        