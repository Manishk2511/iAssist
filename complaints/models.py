from django.db import models

# Create your models here.


class problem(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class complaint(models.Model):
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
    desciption = models.TextField()
    area = models.CharField(max_length=110)
    pincode = models.CharField(max_length=8)
    image = models.ImageField(upload_to="img")
    user = models.IntegerField(default=0)


class latlong(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)


class Complaints(models.Model):
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
    desciption = models.TextField()
    area = models.CharField(max_length=110)
    pincode = models.CharField(max_length=8)
    image = models.ImageField(upload_to="img")
    user = models.IntegerField(default=0)


class image_upload(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to="img")


class otp_verification(models.Model):
    number = models.CharField(max_length=5)

    def __str__(self):
        return self.number
