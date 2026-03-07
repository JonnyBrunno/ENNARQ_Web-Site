from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


# Modelo para guardar informações extras do usuário
class Perfil(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Telefone para contato"
    )

    idade = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    genero = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to='fotos_perfil/',
        default='fotos_perfil/default.jpg',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"


# Modelo de Solicitação de Orçamento
class Orcamento(models.Model):

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_analise', 'Em Análise'),
        ('concluido', 'Concluído'),
    ]

    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orcamentos'
    )

    titulo = models.CharField(
        max_length=200,
        verbose_name="Título da Solicitação"
    )

    descricao = models.TextField(
        verbose_name="Descrição do Problema"
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.titulo} - {self.cliente.username}"


# Modelo de Projetos em andamento
class Projeto(models.Model):

    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projetos'
    )

    nome_projeto = models.CharField(
        max_length=200
    )

    descricao = models.TextField()

    progresso = models.IntegerField(
    default=0,
    validators=[MinValueValidator(0), MaxValueValidator(100)],
    help_text="Progresso do projeto em porcentagem"
)
    data_inicio = models.DateField()

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.nome_projeto} - {self.cliente.username}"
    
@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()