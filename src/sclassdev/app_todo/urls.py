from django.urls import path
from app_todo.views import create , list , read , delete , update

urlpatterns = [
    path('create/' , create.view , name="todo_create"),
    path('list/' , list.view , name='todo_list'),
    path('read/<int:post_id>/' , read.view, name='todo_read'),
    path('delete/<int:post_id>' , delete.view , name='todo_delete'),
    path('update/<int:post_id>' , update.view , name='todo_update'),
]