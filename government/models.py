from django.db import models

# Create your models here.


class area_available(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area


class problem_available(models.Model):
    problem = models.CharField(max_length=100)

    def __str__(self):
        return self.problem


class area_problem_selection(models.Model):
    area_selection = models.ForeignKey(
        area_available, on_delete=models.CASCADE)
    problem_selection = models.ForeignKey(
        problem_available, on_delete=models.CASCADE)
