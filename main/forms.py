from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """Форма для создания и редактирования задач"""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'is_done', 'category', 'executor']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Описание задачи (необязательно)'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'is_done': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'executor': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
