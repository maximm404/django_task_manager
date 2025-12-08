from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('toggle/<int:pk>/', views.task_toggle_status, name='task_toggle_status'),
]
