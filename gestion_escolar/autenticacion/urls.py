from django.urls import path
from .views import login_view
from . import views


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('profesor/', views.dashboard_profesor, name='dashboard_profesor'),
    path('padre/', views.dashboard_padre, name='dashboard_padre'),
]
