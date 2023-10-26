from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completado', views.completed, name='completado'),
    path('remaining', views.remaining, name='remaining'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<str:task_id>', views.delete_task, name='delete'),
    path('detail/<str:task_id>', views.task_detail, name='task_detail'),
    path('toggle_complete/<str:task_id>', views.toggle_complete, name='toggle_complete'),
    path('remove_task/<str:task_id>', views.remove_task, name='remove_task'),
    path('edit_task/<str:task_id>', views.edit_task, name='edit'),
]