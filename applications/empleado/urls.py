from django.urls import path
from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='home'),   
    path('lista-empleados/', views.ListarEmpleados.as_view(), name='listar'),
    path('detalle_empleado/<pk>/', views.DetalleEmpleado.as_view(), name='detalle'),
    path('eliminar_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar'),
    path('listar_por_depto/<shortname>/', views.ListarEmpDepto.as_view(), name='empleados_depto'),
    path('crear_empleado/', views.CrearEmpleado.as_view(), name='crear'),
    path('editar_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='actualizar'),




    # path('listar_por_depto/', views.ListarEmpleadosDepto.as_view()),
    path('listar_por_depto_get_query/<shortname>/', views.ListarEmpDepto.as_view()),
    path('buscar_empleado/', views.ListarEmpDeptoCaja.as_view()),
    path('listar_con_paginacion/', views.ListarConPagincion.as_view()),
    path('listar_con_habilidades/', views.ListarConHabilidades.as_view()),
    #path('success/', views.SuccesView.as_view(), name='correcto'),

    

   

    
    path('eliminar_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar'),
]
