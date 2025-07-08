from django.shortcuts import render, get_object_or_404, redirect
from .models import Nivel
from .forms import NivelForm

def nivel_list(request):
    niveles = Nivel.objects.all()
    return render(request, 'admin/nivel_list.html', {'niveles': niveles})

def nivel_create(request):
    form = NivelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nivel_list')
    return render(request, 'admin/nivel_form.html', {'form': form})

def nivel_update(request, pk):
    nivel = get_object_or_404(Nivel, pk=pk)
    form = NivelForm(request.POST or None, instance=nivel)
    if form.is_valid():
        form.save()
        return redirect('nivel_list')
    return render(request, 'admin/nivel_form.html', {'form': form})

def nivel_delete(request, pk):
    nivel = get_object_or_404(Nivel, pk=pk)
    if request.method == 'POST':
        nivel.delete()
        return redirect('nivel_list')
    return render(request, 'admin/confirm_delete.html', {'object': nivel})
