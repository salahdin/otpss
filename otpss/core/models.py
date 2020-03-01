from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):
    courseCode = models.CharField(
        verbose_name="assessment course code",
        max_length=10,
        null=False,
        blank=False,
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
        blank=True
    )

    uploadDate = models.DateTimeField(
        verbose_name="date and time of upload",
        null=False,
    )

    user = models.ForeignKey(
        User,
        related_name='assessmentpost',
        on_delete=models.DO_NOTHING,
        null=True,
    )


class Question(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        default=None,
        related_name="assessment",
        on_delete=models.CASCADE
    )
    content = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="content of the question"
    )
    date = models.DateTimeField(
        null=False,
        blank=False
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
                                   on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image')

