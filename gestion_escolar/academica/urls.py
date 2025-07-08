from django.urls import path
from autenticacion.views import dashboard_admin
from academica.views_profesor import dashboard_profesor
# Importaciones de views
from . import views_usuario as vuser
from . import views_alumno as valum
from . import views_curso as vcurso
from . import views_grado as vgrado
from . import views_profesor as vprof
from . import views_materia as vmateria
from . import views_nivel as vnivel

urlpatterns = [
    # Dashboard del Admin y Profesor
    path('dashboard_admin/', dashboard_admin, name='dashboard_admin'),
    path('profesor/dashboard/', dashboard_profesor, name='dashboard_profesor'),
    path('profesor/', vprof.dashboard_profesor, name='dashboard_profesor'),
    path('profesor/notas/registrar/', vprof.registrar_nota, name='prof_registrar_nota'),
    path('profesor/asistencias/registrar/', vprof.registrar_asistencia, name='prof_registrar_asistencia'),

    # AJAX PROFESOR
    path('ajax/cargar-capacidades/', vprof.cargar_capacidades, name='ajax_cargar_capacidades'),
    path('ajax/cargar-temas/', vprof.cargar_temas, name='ajax_cargar_temas'),
    path('ajax/cargar-alumno/', vprof.cargar_alumnos, name='ajax_cargar_alumnos'),

    # CRUD Usuarios
    path('admin/usuarios/', vuser.usuario_list, name='usuario_list'),
    path('admin/usuarios/nuevo/', vuser.usuario_create, name='usuario_create'),
    path('admin/usuarios/<int:pk>/editar/', vuser.usuario_update, name='usuario_update'),
    path('admin/usuarios/<int:pk>/eliminar/', vuser.usuario_delete, name='usuario_delete'),

    # CRUD Alumnos
    path('admin/academica/alumno/', valum.alumno_list, name='alumno_list'),
    path('admin/academica/alumno/nuevo/', valum.alumno_create, name='alumno_create'),
    path('admin/academica/alumno/<int:pk>/editar/', valum.alumno_update, name='alumno_update'),
    path('admin/academica/alumno/<int:pk>/eliminar/', valum.alumno_delete, name='alumno_delete'),

    # CRUD Cursos
    path('admin/cursos/', vcurso.curso_list, name='curso_list'),
    path('admin/cursos/nuevo/', vcurso.curso_create, name='curso_create'),
    path('admin/cursos/<int:pk>/editar/', vcurso.curso_update, name='curso_update'),
    path('admin/cursos/<int:pk>/eliminar/', vcurso.curso_delete, name='curso_delete'),

    # CRUD Grados
    path('admin/academica/grado/', vgrado.grado_list, name='grado_list'),
    path('admin/academica/grados/nuevo/', vgrado.grado_create, name='grado_create'),
    path('admin/academica/grados/<int:pk>/editar/', vgrado.grado_update, name='grado_update'),
    path('admin/academica/grados/<int:pk>/eliminar/', vgrado.grado_delete, name='grado_delete'),
    # CRUD Materias
    path('admin/academica/materia/', vmateria.materia_list, name='materia_list'),
    path('admin/academica/materias/nuevo/', vmateria.materia_create, name='materia_create'),
    path('admin/academica/materias/<int:pk>/editar/', vmateria.materia_update, name='materia_update'),
    path('admin/academica/materias/<int:pk>/eliminar/', vmateria.materia_delete, name='materia_delete'),

    # CRUD Niveles
    path('admin/academica/nivel/', vnivel.nivel_list, name='nivel_list'),
    path('admin/academica/niveles/nuevo/', vnivel.nivel_create, name='nivel_create'),
    path('admin/academica/niveles/<int:pk>/editar/', vnivel.nivel_update, name='nivel_update'),
    path('admin/academica/niveles/<int:pk>/eliminar/', vnivel.nivel_delete, name='nivel_delete'),

    # CRUD Profesores
    path('admin/academica/profesor/', vprof.profesor_list, name='profesor_list'),
    path('admin/academica/profesores/nuevo/', vprof.profesor_create, name='profesor_create'),
    path('admin/academica/profesores/<int:pk>/editar/', vprof.profesor_update, name='profesor_update'),
    path('admin/academica/profesores/<int:pk>/eliminar/', vprof.profesor_delete, name='profesor_delete'),
]
