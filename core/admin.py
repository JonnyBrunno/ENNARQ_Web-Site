# core/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Perfil, Orcamento, Projeto

# ====== Perfil ======
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'idade', 'genero', 'foto_preview')
    readonly_fields = ('foto_preview',)
    search_fields = ('user__username', 'telefone', 'genero')

    def foto_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:50%;" />', obj.foto.url)
        return "-"
    foto_preview.short_description = 'Foto'

# ====== Orcamento ======
@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status_colorido', 'data_criacao')
    list_filter = ('status', 'data_criacao')
    search_fields = ('titulo', 'cliente__username')

    def status_colorido(self, obj):
        color = {
            'pendente': 'red',
            'em_analise': 'orange',
            'concluido': 'green'
        }.get(obj.status, 'black')

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_colorido.short_description = 'Status'

# ====== Projeto ======
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'cliente', 'progresso_barra', 'data_inicio')
    search_fields = ('nome_projeto', 'cliente__username')

    def progresso_barra(self, obj):
        return format_html(
            '<div style="background-color:#ddd; width:100px; border-radius:3px;"><div style="width:{}%; background-color:green; text-align:center; color:white; border-radius:3px;">{}%</div></div>',
            obj.progresso, obj.progresso
        )
    progresso_barra.short_description = 'Progresso'