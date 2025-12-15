from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks_list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('toggle/<int:pk>/', views.task_toggle_status, name='task_toggle_status'),
]
