from django.db import models
import uuid

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=40)
    completado = models.BooleanField(default=False)
    description = models.TextField(null=True,blank=True)
    due_date = models.DateField()
    due_time = models.TimeField()


def __str__(self) -> str:
    return f'{self.nombre}'

