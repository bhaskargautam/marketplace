from django.contrib import admin
from main.models import Task, TaskCategory, UserRating

admin.site.register(Task)
admin.site.register(TaskCategory)
admin.site.register(UserRating)