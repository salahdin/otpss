from django.test import TestCase
from .models import *
from faker import Faker
from .forms import *
from django.contrib.auth.models import User


fake = Faker()


class AssessmentTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('testuser', fake.email(), 'password')

    def test_AssessmentForm_invalid(self):
        self.client.login(username='testuser', password='password')
        form = AssessmentForm(data={'courseCode': "", 'courseTitle': "data structure", 'assessmentDate': "2020-03-12",
                                    'user': ""})
        self.assertFalse(form.is_valid())

    def test_AssessmentForm_valid(self):
        self.client.login(username='testuser', password='password')
        form = AssessmentForm(
            data={'courseCode': "CSI247", 'courseTitle': fake.text(), 'assessmentDate': "2020-03-12",
                  'user': self.user})
        self.assertTrue(form.is_valid())

    def test_Question_invalid(self):
        options = {'assessment': "",
                   "content": fake.text(),
                   }
        test_question = Question.objects.create(**options)
        self.assertFalse(isinstance(test_question, Question))


    def test_Question_valid(self):
        self.client.login(username='testuser', password='password')
        assessment = Assessment.object.create(courseCode="CSI247",
                                              courseTitle="title",
                                              assessmentDate="2020-05-04",
                                              user=self.user,
                                              )
        options = {'assessment': assessment,
                "content": fake.text(),
                }
        test_question = Question.objects.create(**options)
        self.assertTrue(isinstance(test_question, Question))

    def test_Answer_invalid(self):
        pass

    def test_Answer_valid(self):
        pass


class AnswerVoteTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', fake.email(), 'bar')
        self.client.login(username='foo', password='bar')

    def test_upvote_same_user(self):
        pass
