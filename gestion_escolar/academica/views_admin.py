from django.shortcuts import render
from academica.models import Rol, Usuario, Nivel, Grado, Materia, Profesor, Alumno

def dashboard_admin(request):
    total_roles = Rol.objects.count()
    total_usuarios = Usuario.objects.count()
    total_niveles = Nivel.objects.count()
    total_grados = Grado.objects.count()
    total_materias = Materia.objects.count()
    total_docentes = Profesor.objects.count()
    total_estudiantes = Alumno.objects.count()

    context = {
        'total_roles': total_roles,
        'total_usuarios': total_usuarios,
        'total_niveles': total_niveles,
        'total_grados': total_grados,
        'total_materias': total_materias,
        'total_docentes': total_docentes,
        'total_estudiantes': total_estudiantes,
    }
    return render(request, 'admin/admin_dashboard.html', context)
