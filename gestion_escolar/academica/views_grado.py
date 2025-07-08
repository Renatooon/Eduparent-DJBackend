# academica/views_grado.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from academica.models import Grado
from academica.forms import GradoForm

@login_required
def grado_list(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    grados = Grado.objects.all()
    return render(request, 'admin/grado_list.html', {'grados': grados})

@login_required
def grado_create(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    form = GradoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('grado_list')
    return render(request, 'admin/grado_form.html', {'form': form, 'action': 'Crear'})

@login_required
def grado_update(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    grado = get_object_or_404(Grado, pk=pk)
    form = GradoForm(request.POST or None, instance=grado)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('grado_list')
    return render(request, 'admin/grado_form.html', {'form': form, 'action': 'Actualizar'})

@login_required
def grado_delete(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    grado = get_object_or_404(Grado, pk=pk)
    if request.method == 'POST':
        grado.delete()
        return redirect('grado_list')
    return render(request, 'admin/confirm_delete.html', {'obj': grado, 'tipo': 'grado'})
