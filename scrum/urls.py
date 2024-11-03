from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('crear-tarea', views.CrearTarea.as_view(), name='crear-tarea'),
    path('listar-tareas', views.ListTareas.as_view(), name='listar-tareas'),
    path('tareas-a-mi-cargo', views.ListTareasACargo.as_view(), name='listar-tareas-a-mi-cargo'),
    path('<int:pk>/editar-tarea', views.EditarTarea.as_view(), name='editar_tarea'),
    path('<int:pk>/eliminar-tarea', views.EliminarTarea.as_view(), name='eliminar_tarea'),
    path('<int:pk>/marcar_completada', views.MarcarComoCompletada.as_view(), name='marcar_completada'),
]