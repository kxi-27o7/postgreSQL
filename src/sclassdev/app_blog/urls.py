from django.urls import path
from app_blog.views import create , list , read , delete , update

urlpatterns = [
    path('create/' , create.view , name="create"),
    path('list/' , list.view , name='list'),
    path('read/<int:post_id>/' , read.view, name='read'),
    path('delete/<int:post_id>' , delete.view , name='blog_delete'),
    path('update/<int:post_id>' , update.view , name='blog_update'),
]