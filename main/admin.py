from django.contrib import admin
from .models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Настройка отображения задач в админке"""
    list_display = ('title', 'is_done', 'deadline', 'category', 'executor', 'created_at')
    list_filter = ('is_done', 'category', 'executor')
    search_fields = ('title', 'description')
    list_editable = ('is_done',)
    date_hierarchy = 'created_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка отображения категорий в админке"""
    list_display = ('name',)
    search_fields = ('name',)
