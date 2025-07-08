from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import NotaForm, AsistenciaForm
from django.contrib.auth import get_user_model
from .models import Curso, Alumno, Nota, Asistencia, Capacidad, Tema, Profesor


# ============================================================
# DASHBOARD DEL PROFESOR
# ============================================================
@login_required
def dashboard_profesor(request):
    usuario = request.user  # Usuario
    profesor = Profesor.objects.get(usuario=usuario)  # Obtener el modelo Profesor

    cursos = Curso.objects.filter(profesor=profesor)
    alumnos = Alumno.objects.filter(grado__curso__in=cursos).distinct()
    asistencias = Asistencia.objects.filter(curso__in=cursos).order_by('-id')
    notas = Nota.objects.filter(curso__in=cursos).order_by('-id')

    context = {
        'total_cursos': cursos.count(),
        'total_alumnos': alumnos.count(),
        'total_asistencias': asistencias.count(),
        'total_notas': notas.count(),
        'asistencias': asistencias[:10],
        'notas': notas,
    }
    return render(request, 'profesor/dashboard.html', context)

# ============================================================
# REGISTRAR NOTA
# ============================================================
@login_required
def registrar_nota(request):
    if request.user.rol != 'profesor':
        return redirect('login')

    form = NotaForm(request.POST or None, user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard_profesor')
        else:
            if form.data.get('competencia'):
                form.fields['capacidad'].queryset = Capacidad.objects.filter(competencia_id=form.data['competencia'])
            if form.data.get('capacidad'):
                form.fields['tema'].queryset = Tema.objects.filter(capacidad_id=form.data['capacidad'])

    return render(request, 'profesor/registrar_nota.html', {"form": form})

# ============================================================
# REGISTRAR ASISTENCIA
# ============================================================
def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, user=request.user)
        if form.is_valid():
            asistencia = form.save(commit=False)
            asistencia.grado = asistencia.alumno.grado
            asistencia.save()
            return redirect('dashboard_profesor')
    else:
        form = AsistenciaForm(user=request.user)
    
    return render(request, 'profesor/registrar_asistencia.html', {'form': form})

# ============================================================
# AJAX: CARGAR CAPACIDADES
# ============================================================
@login_required
def cargar_capacidades(request):
    competencia_id = request.GET.get('competencia_id')
    capacidades = Capacidad.objects.filter(competencia_id=competencia_id).values('id', 'nombre')
    return JsonResponse(list(capacidades), safe=False)

# ============================================================
# AJAX: CARGAR TEMAS
# ============================================================
@login_required
def cargar_temas(request):
    capacidad_id = request.GET.get('capacidad_id')
    temas = Tema.objects.filter(capacidad_id=capacidad_id).values('id', 'nombre')
    return JsonResponse(list(temas), safe=False)



@login_required
def cargar_alumnos(request):
    curso_id = request.GET.get('curso_id')
    alumnos = Alumno.objects.filter(grado__curso__id=curso_id).values('id', 'nombre', 'apellido')
    return JsonResponse(list(alumnos), safe=False)

# === CRUD PARA PROFESOR DESDE PANEL ADMINISTRADOR ===
from .models import Profesor
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfesorForm

def profesor_list(request):
    profesores = Profesor.objects.all()
    User = get_user_model()
    numero_profesores = User.objects.filter(rol='profesor').count()

    return render(request, 'admin/profesor_list.html', {
        'profesores': profesores,
        'numero_profesores': numero_profesores
    })

def profesor_create(request):
    form = ProfesorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profesor_list')
    return render(request, 'admin/profesor_form.html', {'form': form})

def profesor_update(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    form = ProfesorForm(request.POST or None, instance=profesor)
    if form.is_valid():
        form.save()
        return redirect('profesor_list')
    return render(request, 'admin/profesor_form.html', {'form': form})

def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesor_list')
    return render(request, 'admin/profesor_confirm_delete.html', {'profesor': profesor})
