from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .validators import *
from .imagePreProcessing import preProcessImage
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager


class Assessment(models.Model):
    courseCode = models.CharField(
        verbose_name="assessment course code",
        max_length=10,
        null=False,
        blank=False,
        validators=[validate_CourseCode],
    )

    courseTitle = models.CharField(
        verbose_name="course title of assessments",
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
    description = models.TextField(
        verbose_name="assessment description",
        null=True,
        blank=True
    )
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    tags = TaggableManager()

    def __str__(self):
        return self.courseCode


class Question(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        default=None,
        related_name="assessmentQuestion",
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

    def questionSnippet(self):
        return self.content[:25]


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        null=True,
        on_delete=models.CASCADE,
        related_name="questionAnswer",
    )
    Answercontent = models.TextField(
        verbose_name="content of question"
    )
    AnswerImage = models.ImageField(blank=True,null=True,verbose_name="answer image")
    user = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    votes = models.IntegerField(default=0)


voteType = [
    ('U', 'upvote'),
    ('D', 'downvote')
]


class UserVote(models.Model):
    user = models.ForeignKey(User, related_name="user_votes",
                             on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answer, related_name="answer_votes",
                               on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10,
                                 choices=voteType)

    # so users can't up/down-vote twice
    class Meta:
        unique_together = ('user', 'answer', 'vote_type')


class AssessmentImage(models.Model):
    assessment = models.ForeignKey(Assessment,
                                   default=None,
                                   on_delete=models.CASCADE,
                                   related_name="assessmentPic"
                                   )
    image = models.ImageField(verbose_name='Image', upload_to='elements/')

    def save(self, *args, **kwargs):
        self.image = preProcessImage(self.image)
        super().save(*args, **kwargs)


class AssessmentFile(models.Model):
    assessment = models.ForeignKey(Assessment,
                                   default=None,
                                   on_delete=models.CASCADE,
                                   related_name="assessmentdoc"
                                   )

    document = models.FileField(verbose_name="assessment in document format")