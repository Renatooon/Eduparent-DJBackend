from django.db import models
from usuarios.models import Usuario
class Grado(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre


class Seccion(models.Model):
    letra = models.CharField(max_length=1)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grado} - {self.letra}"


class Alumno(models.Model):
    dni      = models.CharField(max_length=8)
    nombre   = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    grado    = models.ForeignKey(Grado, on_delete=models.CASCADE)
    seccion  = models.ForeignKey(Seccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    archivo = models.TextField(blank=True, null=True)  # si tienes ese campo

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido}"


class Curso(models.Model):
    nombre   = models.CharField(max_length=45)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    grado    = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# ----------------------------------
#  ENTIDADES DE EVALUACIÓN
# ----------------------------------

class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    # descripcion = models.TextField()  # Elimina esta línea

    def __str__(self):
        return self.nombre



class Capacidad(models.Model):
    nombre       = models.CharField(max_length=100, default="Sin nombre")
    competencia  = models.ForeignKey(Competencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Tema(models.Model):
    nombre       = models.CharField(max_length=100)
    competencia  = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    capacidad    = models.ForeignKey(Capacidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Evaluacion(models.Model):
    titulo   = models.CharField(max_length=45)
    curso    = models.ForeignKey(Curso, on_delete=models.CASCADE)
    grado    = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Nota(models.Model):
    curso       = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    evaluacion  = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    alumno      = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, null=True, blank=True)
    capacidad   = models.ForeignKey(Capacidad, on_delete=models.CASCADE, null=True, blank=True)
    tema        = models.ForeignKey(Tema, on_delete=models.CASCADE, null=True, blank=True)
    nota        = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} - {self.evaluacion} - {self.nota}"


class Asistencia(models.Model):
    ESTADOS = [
        ('Presente', 'Presente'),
        ('Ausente', 'Ausente'),
        ('Tardanza', 'Tardanza'),
    ]

    semana  = models.IntegerField()
    estado  = models.CharField(max_length=10, choices=ESTADOS)
    alumno  = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso   = models.ForeignKey(Curso, on_delete=models.CASCADE)
    grado   = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asistencia de {self.alumno} en semana {self.semana}"

    
# ---------------------------
# ENTIDADES ADICIONALES (Académica)
# ---------------------------

class Nivel(models.Model):
    """Ejemplo: Inicial, Primaria, Secundaria"""
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    """Asignaturas como Matemática, Comunicación, etc."""
    nombre = models.CharField(max_length=100)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name="materias")

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"
    