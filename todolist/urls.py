from django.urls import  path
from . import views as todolist_views
urlpatterns = [
    path('', todolist_views.todolist, name='todolist'),
    path('delete/<task_id>', todolist_views.delete_task, name='delete_task'),
    path('edit/<task_id>', todolist_views.edit_task, name='edit_task'),
    path('complete/<task_id>', todolist_views.complete_task, name='complete_task'),
    path('pending/<task_id>', todolist_views.pending_task, name='pending_task'),
]