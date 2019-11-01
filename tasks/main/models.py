from django.contrib.auth.models import User
from django.db import models

class TaskCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Task(models.Model):
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

    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    consumer = models.ForeignKey(User, related_name='consumer',
                                      on_delete=models.CASCADE)
    worker = models.ForeignKey(User, default=None, blank=True,
                        related_name='worker', null=True,
                        on_delete=models.CASCADE)

    task_status = models.CharField(
        max_length=1,
        choices=TASK_STATUS,
        default=NEW,
    )

    #Location
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    logitude = models.DecimalField(max_digits=9, decimal_places=6)

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserRating(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'

    RATINGS = [
            (ONE, 'One'),
            (TWO, 'Two'),
            (THREE, 'Three'),
            (FOUR, 'Four'),
            (FIVE, 'Five')
        ]
    for_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='for_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    rating = models.CharField(max_length=1, choices=RATINGS, default=ONE)