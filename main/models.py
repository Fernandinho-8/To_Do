from django.db import models

# Create your models here.
from django.conf import settings 

class Task(models.Model):
    class Priority(models.TextChoices): #textchoices preciso definir como serao minhas escolhas, como serao minhas tasks!!!!
        BAIXA = "B", "Baixa"
        MEDIA = "M", "Media"
        ALTA = "A", "Alta"
        
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, #
        related_name="tasks",
        null=True, #sem valores
        blank=True # permiti que o campo esteja vasio, nao necessariamente precisa ser atrelado a um usuario!!!
    )
    titulo = models.CharField("Titulo", max_length=200) 
    descricao = models.TextField("Descricao", blank=True)
    concluida = models.BooleanField("Concluida", default=False)
    prioridade = models.CharField(
        "Prioridade",
        max_length=1,
        choices=Priority.choices,
        default=Priority.MEDIA,
    )
    data_limite = models.DateField("Data_limite", null=True, blank=True) 
    criado_em = models.DateTimeField("Criado_em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado_em", auto_now=True)

    class Meta:
        ordering = ["concluida", "data_limite", "prioridade", "criado_em"]
        
    def __str__(self)-> str:
        return self.titulo
