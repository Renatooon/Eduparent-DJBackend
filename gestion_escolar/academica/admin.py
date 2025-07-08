from django.contrib import admin
from django import forms
from .models import (
    Grado, Seccion, Alumno, Profesor, Curso, Evaluacion, Nota, Asistencia,
    Competencia, Capacidad, Tema, Materia, Nivel
)
from usuarios.models import Usuario  
# ---------- Formularios personalizados ----------

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'usuario' in self.fields:
            qs = Usuario.objects.filter(
                rol='profesor'  # ← Si `rol` es CharField con choices
            ).exclude(
                id__in=Profesor.objects.values_list('usuario_id', flat=True)
            )

            print("Usuarios disponibles con rol 'profesor':")
            print(list(qs))

            self.fields['usuario'].queryset = qs
# ---------- Registro de modelos ----------
@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['letra', 'grado']

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'apellido', 'grado', 'seccion']
    list_filter = ['grado', 'seccion']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'profesor', 'grado']
    list_filter = ['grado', 'profesor']

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'curso', 'grado']
    list_filter = ['curso', 'grado']

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'evaluacion', 'nota']
    list_filter = ['evaluacion']

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'curso', 'grado', 'semana', 'estado']
    list_filter = ['grado', 'curso', 'semana']

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # 'descripcion' eliminado
@admin.register(Capacidad)
class CapacidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'competencia']
    list_filter = ['competencia']

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad']
    list_filter = ['capacidad']

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel']


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    form = ProfesorForm
    list_display = ['usuario']


