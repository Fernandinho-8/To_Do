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