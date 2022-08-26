from django.shortcuts import render , redirect
from app.forms import TodoForm
from app.models import Todo
# Create your views here.

def Home(request):
    template_name = "index.html"
    items = Todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            
    context  = {
        'items' : items ,
        'form' : form
    }
    return render (request , template_name, context)

def DeleteTodo(request , id):
    template_name = "index.html"
    item = Todo.objects.get(id=id)
    item.delete()
    return redirect('/')