from django.db import models
from django.utils import timezone


# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=200, default=None)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    updated_at = models.DateTimeField(default=timezone.now)
