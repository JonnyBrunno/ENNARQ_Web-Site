from django.db import models
from django.contrib.auth.models import User


class Orcamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_analise', 'Em Análise'),
        ('concluido', 'Concluído'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orcamentos')
    titulo = models.CharField(max_length=200, verbose_name="Título da Solicitação")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.titulo} - {self.cliente.username}"


class Projeto(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos')
    nome_projeto = models.CharField(max_length=200)
    progresso = models.IntegerField(default=0)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome_projeto