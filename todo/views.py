from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):

  if request.method == 'POST':
    new_todo = Todo(title=request.POST['todo_title'])
    new_todo.save()
    return redirect("/")
  all_todos = Todo.objects.all()
  return render(request, "index.html", {"todos": all_todos})


def delete(request, pk):
  todo = Todo.objects.get(id=pk)
  todo.delete()
  return redirect("/")