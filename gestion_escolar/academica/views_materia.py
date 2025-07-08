from django.shortcuts import render, get_object_or_404, redirect
from .models import Materia
from .forms import MateriaForm

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, 'admin/materia_list.html', {'materias': materias})

def materia_create(request):
    form = MateriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('materia_list')
    return render(request, 'admin/materia_form.html', {'form': form})

def materia_update(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    form = MateriaForm(request.POST or None, instance=materia)
    if form.is_valid():
        form.save()
        return redirect('materia_list')
    return render(request, 'admin/materia_form.html', {'form': form})

def materia_delete(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('materia_list')
    return render(request, 'admin/confirm_delete.html', {'object': materia})
