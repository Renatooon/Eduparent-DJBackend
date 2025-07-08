# academica/views_curso.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from academica.models import Curso
from academica.forms import CursoForm

@login_required
def curso_list(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    cursos = Curso.objects.select_related('profesor', 'grado')
    return render(request, 'admin/curso_list.html', {'cursos': cursos})

@login_required
def curso_create(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    form = CursoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request, 'admin/curso_form.html', {'form': form, 'action': 'Crear'})

@login_required
def curso_update(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request, 'admin/curso_form.html', {'form': form, 'action': 'Actualizar'})

@login_required
def curso_delete(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'admin/confirm_delete.html', {'obj': curso, 'tipo': 'curso'})
