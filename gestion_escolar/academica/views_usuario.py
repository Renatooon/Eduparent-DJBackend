# academica/views_usuario.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from academica.forms import UsuarioForm    # ya lo creaste en forms.py

# ----------------------- LISTAR -----------------------
@login_required
def usuario_list(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    usuarios = Usuario.objects.all()
    return render(request, 'admin/usuario_list.html', {'usuarios': usuarios})

# ----------------------- CREAR ------------------------
@login_required
def usuario_create(request):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('usuario_list')
    return render(request, 'admin/usuario_form.html', {'form': form, 'action': 'Crear'})

# ----------------------- EDITAR -----------------------
@login_required
def usuario_update(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('usuario_list')
    return render(request, 'admin/usuario_form.html', {'form': form, 'action': 'Actualizar'})

# ----------------------- ELIMINAR ---------------------
@login_required
def usuario_delete(request, pk):
    if request.user.rol != 'administrador':
        return redirect('dashboard_admin')
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'admin/confirm_delete.html', {'obj': usuario, 'tipo': 'usuario'})
