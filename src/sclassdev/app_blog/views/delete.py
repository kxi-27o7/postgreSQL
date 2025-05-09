from django.shortcuts import render , redirect
from app_blog.utility import query

def view(request , post_id):
    if request.method == 'GET':
        post = query('DELETE FROM blog_post WHERE ID = %s' , [post_id])
        print(post)

    return redirect('/blog/list/' , name='blog_list')