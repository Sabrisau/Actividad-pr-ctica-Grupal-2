from django.shortcuts import get_object_or_404, render
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Tarea

def home(request):
    return render(request, 'home.html')

class CrearTarea(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'criterios_aceptacion', 'prioridad', 'estado', 'esfuerzo_estimado', 'responsable', 'sprint_asignado', 'dependencias', 'bloqueadores']
    template_name = 'crear_tarea.html'
    success_url = reverse_lazy('listar-tareas')
    permission_required = 'scrum.add_epica', 'scrum.view_epica', 'scrum.add_sprint', 'scrum.view_sprint', 'scrum.add_tarea', 'scrum.view_tarea'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permisos'] = self.request.user.get_all_permissions
        return context

class ListTareas(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tarea
    context_object_name= 'tareas'
    template_name = 'listar_todas.html'
    permission_required = ('scrum.view_epica', 'scrum.view_sprint', 'scrum.view_tarea')

    def get_queryset(self):
        # usamos select_related para que DJango no realice una consulta adicional 
        # a la hora de mostrar las tareas en las plantillas
        return Tarea.objects.select_related('sprint_asignado').all() 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permisos'] = self.request.user.get_all_permissions
        return context

class ListTareasACargo(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tarea
    context_object_name= 'tareas'
    template_name = 'listar_todas.html'
    permission_required = ('scrum.view_epica', 'scrum.view_sprint', 'scrum.view_tarea')

    def get_queryset(self):
        return Tarea.objects.select_related('sprint_asignado').filter(responsable=self.request.user) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permisos'] = self.request.user.get_all_permissions
        return context

class EditarTarea(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'criterios_aceptacion', 'prioridad', 'estado', 'esfuerzo_estimado', 'responsable', 'sprint_asignado', 'dependencias', 'bloqueadores']
    template_name = 'editar_tarea.html'
    success_url = reverse_lazy('listar-tareas')
    permission_required = ('scrum.change_epica', 'scrum.change_sprint', 'scrum.change_tarea')

    def form_valid(self, form):
        form.instance.responsable = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permisos'] = self.request.user.get_all_permissions
        return context
    
class EliminarTarea(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar_tarea.html'
    success_url = reverse_lazy('listar-tareas')
    permission_required = ('scrum.delete_epica', 'scrum.delete_sprint', 'scrum.delete_tarea')