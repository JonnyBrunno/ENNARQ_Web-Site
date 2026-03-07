from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.register_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('minha-conta/', views.area_cliente, name='area_cliente'),
    path('solicitar/', views.solicitar_orcamento, name='solicitar_orcamento'),
]