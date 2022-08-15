from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from usuarios import views
from rest_framework.authtoken import views as auth_views
 
urlpatterns=[
   # path('registrarUsuario/', views.registrar_usuario, name="registrar_usuario"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
