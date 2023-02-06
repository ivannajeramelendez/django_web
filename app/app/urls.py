"""
Configuración de la URL de la aplicación
    Ejemplos:
    Vistas de función
        1. Agregue una importación: desde las vistas de importación de my_app
        2. Agregue una URL a urlpatterns: path('', views.home, name='home')
    Vistas basadas en clases
        1. Agregue una importación: from other_app.views import Home
        2. Agrega una URL a urlpatterns: path('', Home.as_view(), name='home')
    Incluir otra URLconf
        1. Importe la función include(): desde django.urls import include, ruta
        2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# SERVICIOS
from dashboard import views

urlpatterns = [
    path('', views.inicio),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
