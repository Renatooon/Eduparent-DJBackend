# academica/views_alumno.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from academica.models import Alumno
from academica.forms import AlumnoForm

@login_required
def alumno_list(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    alumnos = Alumno.objects.select_related('grado', 'seccion')
    return render(request, 'admin/alumno_list.html', {'alumnos': alumnos})

@login_required
def alumno_create(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    form = AlumnoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alumno_list')
    return render(request, 'admin/alumno_form.html', {'form': form, 'action': 'Crear'})

@login_required
def alumno_update(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    alumno = get_object_or_404(Alumno, pk=pk)
    form = AlumnoForm(request.POST or None, instance=alumno)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alumno_list')
    return render(request, 'admin/alumno_form.html', {'form': form, 'action': 'Actualizar'})

@login_required
def alumno_delete(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_list')
    return render(request, 'admin/confirm_delete.html', {'obj': alumno, 'tipo': 'alumno'})
