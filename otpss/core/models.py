from django.db import models


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


class Question(models.Model):
    pass


class Answer(models.Model):
    pass


class Image(models.Model):
    pass