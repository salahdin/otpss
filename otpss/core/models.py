from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from .convert import convert_img_to_txt
from .validators import *


class Assessment(models.Model):
    courseCode = models.CharField(
        verbose_name="assessment course code",
        max_length=10,
        null=False,
        blank=False,
        validators=[validate_CourseCode],
    )

    courseTitle = models.CharField(
        verbose_name="course title of assessment",
        max_length=100,
        null=True,
        blank=True,
    )

    assessmentDate = models.DateField(
        verbose_name="day of assessment",
        null=True,
        blank=True,
        validators=[validate_AssessmentDate],
    )

    uploadDate = models.DateTimeField(
        verbose_name="date and time of upload",
        null=False,
        auto_created=True,
        default=timezone.now
    )

    user = models.ForeignKey(
        User,
        related_name='assessmentPost',
        on_delete=models.DO_NOTHING,
        null=True,
    )

    votes = models.IntegerField(default=0)


class UserVotes(models.Model):
    user = models.ForeignKey(User, related_name="user_votes")
    assessment = models.ForeignKey(Assessment, related_name="post_votes")
    vote_type = models.CharField()

    class Meta:
        unique_together = ('user', 'post', 'vote_type')


class Question(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        default=None,
        related_name="assessment",
        on_delete=models.CASCADE,
        unique=False
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="content of the question"
    )
    date = models.DateTimeField(
        null=False,
        blank=False,

    )


class Answer(models.Model):
    question = models.ManyToManyField(
        Question,
        related_name="question",
    )

    Answercontent = models.CharField(
        max_length=500,
        verbose_name="content of question"
    )

    user = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True, verbose_name="date created")


class AssessmentImage(models.Model):
    assessment = models.ForeignKey(Assessment,
                                   default=None,
                                   on_delete=models.CASCADE,
                                   related_name="assessmentPic"
                                   )
    image = models.ImageField(verbose_name='Image', upload_to='elements/')
