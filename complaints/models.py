from django.db import models

# Create your models here.


class problem(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class complaint(models.Model):
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
    desciption = models.TextField()
    area = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
