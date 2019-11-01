from django.contrib import admin
from main.models import Task, TaskCategory

admin.site.register(Task)
admin.site.register(TaskCategory)