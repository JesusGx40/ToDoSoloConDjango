from django import forms
from .models import Task

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nombre', 'description', 'due_date', 'completado','due_time']
