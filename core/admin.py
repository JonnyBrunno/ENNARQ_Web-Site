from django.contrib import admin
from .models import Orcamento, Projeto

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status', 'data_criacao')
    list_filter = ('status', 'data_criacao')
    search_fields = ('titulo', 'cliente__username')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'cliente', 'progresso', 'data_inicio')
    search_fields = ('nome_projeto', 'cliente__username')
