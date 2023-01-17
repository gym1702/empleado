from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Empleado
from .forms import EmpleadoForm

#****************************************************
#                      LISTVIEW
#****************************************************

# VISTA HOME
class InicioView(TemplateView):
    template_name = "home.html"


#LISTA TODOS LOS EMPLEADOS
class ListarEmpleados(ListView):
    #model = Empleado (este no va si se utiliza buscador de caja de texto)
    paginate_by = 5
    ordering = 'first_name'
    template_name = "empleado/listar.html"
    context_object_name = 'obj'

    #Filtro de busqueda con caja de texto
    def get_queryset(self):
        palabra_clave = self.request.GET.get("valor", '')
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)
        return lista



#METDODO QUERYSET
# class ListarEmpleadosDepto(ListView):
#     queryset = Empleado.objects.filter(department__short_name='Sistemas')
#     template_name = "empleado/listar_por_depto.html"
#     context_object_name = 'obj'



#METODO GET_QUERYSET CON PARAMETROS
class ListarEmpDepto(ListView):
    template_name = "empleado/listar_por_depto.html"
    context_object_name = 'obj'

    def get_queryset(self):
        depto =  self.kwargs['shortname']
        lista = Empleado.objects.filter(department__short_name=depto)
        return lista



#METODO BUSQUEDA POR CAJA DE TEXTO
class ListarEmpDeptoCaja(ListView):
    template_name = "empleado/listar_por_depto_caja.html"
    context_object_name = 'obj'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista
        

#LISTAR CON PAGINACION
class ListarConPagincion(ListView):
    model = Empleado
    template_name = "empleado/listar_con_paginacion.html"
    context_object_name = 'obj'
    paginate_by = 4


#LISTAR CON RELACION MUCHOS A MUCHOS
class ListarConHabilidades(ListView):
    model = Empleado
    template_name = "empleado/listar_con_habilidades.html"
    context_object_name = 'obj'

    def get_queryset(self):
        id_empleado = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(id=id_empleado)
        return (empleado.habilidades.all())


#****************************************************
#                      DETAILVIEW
#****************************************************

class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = "empleado/detalle_empleado.html"
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(DetalleEmpleado, self).get_context_data(**kwargs)
        return context


#****************************************************
#                      CREATEVIEW
#****************************************************

#VISTA TEMPORAL PARA REDIRECCION DESPUES DE CREAR
# class SuccesView(TemplateView):
#     template_name = "empleado/success.html"


#GUARDADO DE INFORMACION
class CrearEmpleado(CreateView):
    model = Empleado
    template_name = "empleado/crear_empleado.html"
    #fields = ['first_name', 'last_name', 'job', 'department', 'habilidades',]
    form_class = EmpleadoForm
    context_object_name = 'obj'
    success_url = reverse_lazy('empleado_app:listar')

    #OPCION PARA GUARDAR ALGO DESPUES DE GUARDAR (NO NECESARIA PARA EL GUARDADO)
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(CrearEmpleado, self).form_valid(form)


#****************************************************
#                      UPDATEVIEW
#****************************************************
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/actualizar.html"
    #fields = ['first_name', 'last_name', 'job', 'department', 'habilidades',]
    form_class = EmpleadoForm
    context_object_name = 'obj'
    success_url = reverse_lazy('empleado_app:listar')

    #OPCIONAL PARA GUARDAR DESPUES DEL GUARDADO
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


#****************************************************
#                      DELETEVIEW
#****************************************************
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/eliminar.html"
    success_url = reverse_lazy('empleado_app:listar')
