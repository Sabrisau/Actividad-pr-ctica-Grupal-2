from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('crear-tarea', views.CrearTarea.as_view(), name='crear-tarea'),
    path('listar-tareas', views.ListTareas.as_view(), name='listar-tareas'),
    path('tareas-a-mi-cargo', views.ListTareasACargo.as_view(), name='listar-tareas-a-mi-cargo'),
]