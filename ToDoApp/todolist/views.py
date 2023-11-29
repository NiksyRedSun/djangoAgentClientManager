from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Tasks

from django.views.decorators.http import require_http_methods

from django.contrib import messages




# Create your views here.



def index(request):
    todos = Tasks.objects.all()
    return render(request, "todolist/index.html", {'todo_list': todos, 'title': "Главная страница"})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    if not title:
        messages.error(request, 'Задача не может быть пустой')
    else:
        todo = Tasks(title=title)
        todo.save()
        messages.success(request, 'Успешно сохранено')
    return redirect('index')


def update(request, todo_id):
    todo = Tasks.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Tasks.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')