from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Category
from .forms import TaskForm


class TaskListView(ListView):
    """Список задач с фильтрацией, поиском и пагинацией"""
    model = Task
    template_name = 'main/tasks_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.all()

        # Фильтрация по категории
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        # Фильтрация по статусу
        status = self.request.GET.get('status')
        if status == 'done':
            queryset = queryset.filter(is_done=True)
        elif status == 'not_done':
            queryset = queryset.filter(is_done=False)

        # Поиск по названию
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class TaskDetailView(DetailView):
    """Детальный просмотр задачи"""
    model = Task
    template_name = 'main/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Создание новой задачи"""
    model = Task
    form_class = TaskForm
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('tasks_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание задачи'
        return context

    def form_valid(self, form):
        form.instance.executor = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование задачи"""
    model = Task
    form_class = TaskForm
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('tasks_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование задачи'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление задачи"""
    model = Task
    template_name = 'main/task_confirm_delete.html'
    success_url = reverse_lazy('tasks_list')
    context_object_name = 'task'


def task_toggle_status(request, pk):
    """Быстрое переключение статуса задачи"""
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('tasks_list')