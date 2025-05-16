from django.shortcuts import render , redirect
from app_todo.utility import query

def view(request , post_id):
    post = query("SELECT * FROM todo_post WHERE id = %s" , [post_id])
    print(post)

    if not post:
        return render(request , 'app_todo/notfound.html' , status=404)

    if request.method == 'GET':
        return render(request, 'app_todo/update.html', {'post' : post[0]})

    if request.method == 'POST':
        
        post = post[0]

        title = request.POST.get('title')
        content = request.POST.get('content')

        query("UPDATE todo_post SET title = %s, content = %s WHERE id = %s" , [title , content , post_id])

        return redirect(f"/todo/read/{post_id}/")
    
    return render(request , 'app_todo/update.html' , {'post' : post})