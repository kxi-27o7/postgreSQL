from django.shortcuts import render , redirect
from app_todo.utility import query

def view(request , post_id):
    if request.method == 'GET':
        post = query('DELETE FROM todo_post WHERE ID = %s' , [post_id])
        print(post)

    return redirect('/todo/list/' , name='todo_list')