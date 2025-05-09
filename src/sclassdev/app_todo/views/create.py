from django.shortcuts import render
from app_todo.utility import query

def view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        result = query("INSERT INTO todo_post (title , desc) VALUES (%s , %s)" , [title , desc])
        print(result)
        
    return render(request , 'app_todo/create.html')