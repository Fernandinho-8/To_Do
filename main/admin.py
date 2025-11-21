from django.contrib import admin

# Register your models here.
from main.models import Task
#admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'usuario',)
    list_filter = ('concluida', 'prioridade',)
    search_fields = ('titulo',)