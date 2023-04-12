from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(request, 'todos/index.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST, request.FILES)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.author = request.user
                todo.save()
                return redirect('todos:index')

        else:
            form = TodoForm()
        
        context = {'form': form}
        return render(request, 'todos/create.html', context)
    else:
        return render(request, 'accounts/login.html')

def complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == False:
        todo.completed = True
        
    else:
        todo.completed = False
    todo.save()

    return redirect('todos:index')

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('todos:index')