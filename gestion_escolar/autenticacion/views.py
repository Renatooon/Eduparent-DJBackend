from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from academica.models import Asistencia, Grado, Curso, Alumno, Nota, Profesor, Nivel, Materia


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.rol == 'administrador':
                return redirect('dashboard_admin')
            elif user.rol == 'profesor':
                return redirect('dashboard_profesor')
            elif user.rol == 'padre':
                return redirect('dashboard_padre')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


@login_required
def dashboard_admin(request):
    context = {
        'total_usuarios': Usuario.objects.count(),
        'total_niveles': Nivel.objects.count(),
        'total_grados': Grado.objects.count(),
        'total_materias': Materia.objects.count(),
        'total_docentes': Usuario.objects.filter(rol='profesor').count(),
        'total_estudiantes': Alumno.objects.count(),
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def dashboard_profesor(request):
    usuario = request.user  # Usuario autenticado
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
        'notas': notas[:10],
    }
    return render(request, 'profesor/dashboard.html', context)
@login_required
def dashboard_padre(request):
    return render(request, 'padre_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
