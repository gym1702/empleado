from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    #path('crear_depto/', views.NuevoDepartamento.as_view(), name='crear_depto'),

    path('listar_depto/', views.DepartamentosListView.as_view(), name='listar'),
    path('eliminar_depto/<pk>', views.DepartamentoDeleteView.as_view(), name='eliminar'),
    path('crear_depto/', views.CrearDepto.as_view(), name='crear'),
    path('crear_depto/<pk>', views.DeptoUpdateView.as_view(), name='editar'),

    path('crear_depto_emp/', views.NuevoDepartamento.as_view(), name='crear_depto_emp'),

]
