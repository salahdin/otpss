from django.db import models
from django.contrib.auth.models import User
from . import courseList


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentId = models.IntegerField(verbose_name="student id")
    program = models.CharField(max_length=100,
                               verbose_name="program user registered for")

    def __str__(self):
        return str(self.studentId)
