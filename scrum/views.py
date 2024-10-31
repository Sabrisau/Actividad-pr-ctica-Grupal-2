from django.shortcuts import render
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea

def home(request):
    return render(request, 'home.html')

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'criterios_aceptacion', 'prioridad', 'estado', 'esfuerzo_estimado', 'responsable', 'sprint_asignado', 'dependencias', 'bloqueadores']
    template_name = 'crear_tarea.html'
    success_url = reverse_lazy('listar-tareas')

    def form_valid(self, form):
        return super().form_valid(form)


class ListTareas(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name= 'tareas'
    template_name = 'listar_todas.html'

    def get_queryset(self):
        # usamos select_related para que DJango no realice una consulta adicional 
        # a la hora de mostrar las tareas en las plantillas
        return Tarea.objects.select_related('sprint_asignado').all() 

class ListTareasACargo (LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name= 'tareas'
    template_name = 'listar_todas.html'

    def get_queryset(self):
        return Tarea.objects.select_related('sprint_asignado').filter(responsable=self.request.user) 
