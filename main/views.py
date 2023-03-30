from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoItemForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def todo_list(request):
    todo_items = TodoItem.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo_list.html', {'todo_items': todo_items})


@login_required
def todo_item(request, id):
    todo_item = TodoItem.objects.get(id=id)
    return render(request, 'todo_item.html', {'todo_item': todo_item})


@login_required
def add_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    context = {
        'form': form,
    }
    return render(request, 'add_todo_item.html', context)


@login_required
def edit_todo_item(request, id):
    todo_item = get_object_or_404(TodoItem, id=id, user=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo_item)
    context = {
        'form': form,
        'todo_item': todo_item,
    }

    return render(request, 'edit_todo_item.html', context )


@login_required
def delete_todo_item(request, id):
    todo_item = get_object_or_404(TodoItem, id=id, user=request.user)
    todo_item.delete()
    return redirect('todo_list')

