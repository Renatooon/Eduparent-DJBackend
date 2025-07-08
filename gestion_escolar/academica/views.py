from django.shortcuts import render, redirect
from .forms import NotaForm
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

@login_required
def registrar_nota(request):
    if request.user.rol != 'profesor':
        return redirect('no_autorizado')  # opción de seguridad

    form = NotaForm(request.POST or None, user=request.user)
    
    if request.method == 'POST':
        if form.is_valid():
            nota = form.save(commit=False)
            nota.save()
            return redirect('lista_notas')

    return render(request, 'profesor/registrar_nota.html', {'form': form})



