from django.urls import path
from . import views

app_name = 'pruebas_app'

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.List.as_view()),
    path('lista-prueba/', views.ListaPrueba.as_view()),

    path('crear-prueba/', views.PruebaCreateView.as_view(), name='crear'),

]
