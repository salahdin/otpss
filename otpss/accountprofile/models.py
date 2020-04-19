from django.db import models
from django.contrib.auth.models import User
from . import finallist


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    studentId = models.IntegerField(verbose_name="student id")
    program = models.CharField(max_length=100,
                               verbose_name="program user registered for",
                               choices=finallist.programList
                               )
    avatar = models.ImageField(verbose_name="user avatar", upload_to='profile/', null=True)

    def __str__(self):
        return str(self.studentId)
