from os import name
from django.urls import path
from main import views
from main.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name='task_list'), 
    path('funcao/', views.task_list, name='task_list'),
    path('task_concluido', views.task_concluido, name='task_concluido'),
    path('task_nao_concluido', views.task_nao_concluido, name='task_nao_concluido')

]
