from django.shortcuts import render, redirect
from .models import Todos,Categories
from .forms import TodoForm,CategoryForm,TodoCompletedForm
from django.views.generic import DeleteView

# Create your views here.


def todos_display(request):
    if request.method=='POST':
        todo_form = TodoForm(request.POST,prefix="todo")
        category_form=CategoryForm(request.POST,prefix="category")
        if 'submit_todo' in request.POST and todo_form.is_valid():
            todo_form.save()
            return redirect('todos:todo_list')
        elif 'submit_category' in request.POST and category_form.is_valid():
            category_form.save()
            return redirect('todos:todo_list')
        elif 'todo_id' in request.POST:
            todo_id = request.POST['todo_id']
            completed = 'completed' in request.POST
            todo = Todos.objects.get(id=todo_id)
            todo.completed =  True
            print("yahh")
            todo.save()
        elif 'delete' in request.POST:
            Todos.objects.filter(completed=True).delete()
        elif 'cat_id' in request.POST:
            cat_id = request.POST['cat_id']
            Categories.objects.filter(id=cat_id).delete()


    else:
        print("yahh4")
        todo_form=TodoForm(prefix="todo")
        category_form = CategoryForm(prefix="category")
    categories = Categories.objects.all()
    todos = Todos.objects.all()
    context={
        "categories" : categories,
        "todos" : todos,
        'todo_form' : todo_form,
        'category_form' : category_form,
    }
    return render(request,'todos/todo_list.html',context)


