from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Task #ijmportar a atbela que agente vai tranbalhar

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView): #possibilitar minha interaçao com o 
    template_name = 'home.html'
    
class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas' # como eu defino como eu quero ver os dados sendo mostrados no frontend

#views---url---template


def task_list(request):
    tarefas = Task.objects.all()
    context = {
        "tarefas":tarefas,
        "titulo_pagina": 'Minhas Tarefas'
    }
    return render(request, 'tasks/task_list.html', context)

def task_concluido(request):
    tarefas = Task.objects.filter(concluida=1)
    context = {
        "tarefas":tarefas,
        "titulo_pagina": 'Minhas Tarefas Concluidas',
    }
    return render(request, 'tasks/teste.html', context)

def task_nao_concluido(request):
    tarefas = Task.objects.filter(concluida=0)
    context = {
        "tarefas":tarefas,
        "titulo_pagina": 'Minhas Tarefas nao concluidas',
    }
    return render(request, 'tasks/teste.html', context)