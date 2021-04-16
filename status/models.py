from django.db import models
from complaints.models import Complaints
from django.utils import timezone
time = timezone.localtime()
# Create your models here.


class status_type(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class user_status_type(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Complaint_Update(models.Model):
    status = models.ForeignKey(status_type, on_delete=models.CASCADE)
    update_id = models.AutoField(primary_key=True)
    complaint_id = models.IntegerField()
    desc = models.CharField(max_length=2000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class user_status_list(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    status = models.ForeignKey(user_status_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class status_list(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    status = models.ForeignKey(status_type, on_delete=models.CASCADE)
    # time = models.DateTimeField(_('Create DateTime'), auto_now_add=True)

    def __str__(self):
        return self.status
