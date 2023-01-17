from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import NuevoDepartamento
from applications.empleado.models import Empleado
from .models import Departamento
from .forms import DeptoForm


#FORMVIEW SE UTILIZA PARA TRABAJAR CON VARIOS MODELOS A LA VEZ
class NuevoDepartamento(FormView):
    template_name = 'departamento/crearconempleado.html'
    form_class = NuevoDepartamento
    success_url = reverse_lazy('departamento_app:listar')

    def form_valid(self, form):      
        #Guardado de departamento  
        depto = Departamento (
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['nombrecorto'],
        )
        depto.save()

        #Guardado de empleado
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre, 
            last_name = apellidos,
            full_name = nombre + ' ' + apellidos,
            job = 1,
            department = depto,
        )

        return super(NuevoDepartamento, self).form_valid(form)


#****************************************************
#                      LISTAR
#****************************************************
class DepartamentosListView(ListView):
    template_name = "departamento/listar.html"
    context_object_name = 'obj'
    paginate_by = 5
    ordering = 'first_name'

    #Filtro de busqueda con caja de texto
    def get_queryset(self):
        palabra_clave = self.request.GET.get("valor", '')
        lista = Departamento.objects.filter(name__icontains=palabra_clave)
        return lista


#****************************************************
#                      DETALLES
#****************************************************
class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = "empleado/detalle_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(DetalleEmpleado, self).get_context_data(**kwargs)
        return context


#****************************************************
#                      CREATEVIEW
#****************************************************
#GUARDADO DE INFORMACION
class CrearDepto(CreateView):
    model = Departamento
    template_name = "departamento/crear.html"
    form_class = DeptoForm
    success_url = reverse_lazy('departamento_app:listar')


#****************************************************
#                      UPDATEVIEW
#****************************************************
class DeptoUpdateView(UpdateView):
    model = Departamento
    template_name = "departamento/actualizar.html"
    form_class = DeptoForm
    success_url = reverse_lazy('departamento_app:listar')


#****************************************************
#                      ELIMINAR
#****************************************************
class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = "departamento/eliminar.html"
    success_url = reverse_lazy('departamento_app:listar')



