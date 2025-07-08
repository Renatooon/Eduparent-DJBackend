from django import forms
from usuarios.models import Usuario 
from .models import Grado, Materia, Nivel, Nota, Evaluacion, Competencia, Capacidad, Profesor, Tema
from .models import Asistencia, Alumno, Curso, Seccion


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['curso', 'evaluacion', 'alumno',
                  'competencia', 'capacidad', 'tema', 'nota']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            try:
                profesor = Profesor.objects.get(usuario=user)
                cursos_prof = Curso.objects.filter(profesor=profesor)
                grados = cursos_prof.values_list('grado', flat=True)
                self.fields['curso'].queryset = cursos_prof
                self.fields['alumno'].queryset = Alumno.objects.filter(grado_id__in=grados).distinct()
            except Profesor.DoesNotExist:
                self.fields['curso'].queryset = Curso.objects.none()
                self.fields['alumno'].queryset = Alumno.objects.none()
        else:
            self.fields['curso'].queryset = Curso.objects.none()
            self.fields['alumno'].queryset = Alumno.objects.none()

        self.fields['evaluacion'].queryset = Evaluacion.objects.all()
        self.fields['capacidad'].queryset = Capacidad.objects.none()
        self.fields['tema'].queryset = Tema.objects.none()

        if 'competencia' in self.data:
            try:
                competencia_id = int(self.data.get('competencia'))
                self.fields['capacidad'].queryset = Capacidad.objects.filter(competencia_id=competencia_id)
            except (ValueError, TypeError):
                pass

        if 'capacidad' in self.data:
            try:
                capacidad_id = int(self.data.get('capacidad'))
                self.fields['tema'].queryset = Tema.objects.filter(capacidad_id=capacidad_id)
            except (ValueError, TypeError):
                pass

        if 'curso' in self.data:
            try:
                curso_id = int(self.data.get('curso'))
                curso = Curso.objects.get(id=curso_id)
                self.fields['alumno'].queryset = Alumno.objects.filter(grado=curso.grado)
            except (ValueError, TypeError, Curso.DoesNotExist):
                self.fields['alumno'].queryset = Alumno.objects.none()

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if nota is not None and (nota < 0 or nota > 20):
            raise forms.ValidationError("La nota debe estar entre 0 y 20.")
        return nota

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['curso', 'alumno', 'semana', 'estado']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            try:
                profesor = Profesor.objects.get(usuario=user)
                self.fields['curso'].queryset = Curso.objects.filter(profesor=profesor)
            except Profesor.DoesNotExist:
                self.fields['curso'].queryset = Curso.objects.none()
        else:
            self.fields['curso'].queryset = Curso.objects.none()

        self.fields['alumno'].queryset = Alumno.objects.none()

        if 'curso' in self.data:
            try:
                curso_id = int(self.data.get('curso'))
                curso = Curso.objects.get(id=curso_id)
                self.fields['alumno'].queryset = Alumno.objects.filter(grado=curso.grado)
            except (ValueError, TypeError, Curso.DoesNotExist):
                pass
        elif self.instance.pk:
            self.fields['alumno'].queryset = Alumno.objects.filter(grado=self.instance.curso.grado)

        self.fields['alumno'].label_from_instance = (
            lambda obj: f"{obj.nombre} {obj.apellido}"
        )


# === CRUDs del dashboard administrador ===

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'apellido', 'grado', 'seccion']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['archivo', 'usuario']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'profesor', 'grado']

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nombre']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'rol']

class SeccionForm(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ['letra', 'grado']
        labels = {
            'letra': 'Letra / Sección',
            'grado': 'Grado asociado',
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = '__all__'
