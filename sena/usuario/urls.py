from django.urls import path
from .views import (
    ListarUsuariosView,
    CrearUsuarioView,
    EditarUsuarioView,
    EliminarUsuarioView,
    CambiarEstadoUsuarioView,
)

app_name = 'usuario'

urlpatterns = [
    path('listar/',            ListarUsuariosView.as_view(),       name='listar'),
    path('crear/',             CrearUsuarioView.as_view(),         name='crear'),
    path('editar/<int:pk>/',   EditarUsuarioView.as_view(),        name='editar'),
    path('eliminar/<int:pk>/', EliminarUsuarioView.as_view(),      name='eliminar'),
    path('estado/<int:pk>/',   CambiarEstadoUsuarioView.as_view(), name='estado'),
]