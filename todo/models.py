from django.db import models

# Create your models here.

PRIORITY = (('danger', 'high'), ('secondary', 'normal'), ('light', 'low'))


class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title