from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('crear_tienda/', views.crear_tienda, name='crear_tienda'),
    path('consultar_base_datos/', views.consultar_base_datos, name='consultar_base_datos'),
]
