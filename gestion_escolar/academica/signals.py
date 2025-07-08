from django.db.models.signals import post_save
from django.dispatch import receiver
from academica.models import Profesor
from usuarios.models import Usuario  # Cambia esto si tu modelo Usuario está en otra app
@receiver(post_save, sender=Usuario)
def crear_profesor_automatico(sender, instance, created, **kwargs):
    try:
        rol_nombre = instance.rol.nombre.lower()
    except AttributeError:
        rol_nombre = str(instance.rol).lower()  # en caso de que sea un string

    if created and rol_nombre == "profesor":
        if not Profesor.objects.filter(usuario=instance).exists():
            Profesor
