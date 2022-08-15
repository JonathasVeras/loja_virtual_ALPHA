from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from localizacoes import views
from rest_framework.authtoken import views as auth_views

urlpatterns=[
    path('PaisList/', views.PaisList.as_view(), name="lista-pais"),
    path('EstadoList/', views.EstadoList.as_view(), name="lista-Estado"),
    path('CidadeList/', views.CidadeList.as_view(), name="lista-Cidade"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
