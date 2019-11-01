from django.contrib.auth.models import User
from django.db import models

class TaskCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

class Tasks(models.Model):
    NEW = 'N'
    PENDING = 'P'
    COMPLETED = 'C'

    TASK_STATUS = [
        (NEW, 'New'),
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    consumer = models.ForeignKey(TaskCategory)
    consumer = models.ForeignKey(User) #on_delete=models.CASCADE)
    worker = models.ForeignKey(User, default=None, blank=True, null=True) #on_delete=models.CASCADE)

    task_status = models.CharField(
        max_length=1,
        choices=TASK_STATUS,
        default=NEW,
    )

    #Location
    latitude = DecimalField(max_digits=9, decimal_places=6)
    logitude = DecimalField(max_digits=9, decimal_places=6)

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

""" Todo: Rating Model.
class UserRating(models.Model):
    for_user = models.ForeignKey(User)
    from_user = models.ForeignKey(User)
    rating = models.CharField(max_length=1)
"""