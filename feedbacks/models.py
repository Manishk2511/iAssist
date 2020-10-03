from django.db import models
from complaints.models import problem
# Create your models here.


class Feedback(models.Model):
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    pincode = models.IntegerField()
    feedback = models.TextField()
