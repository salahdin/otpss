from django.test import TestCase
from .models import *
from faker import Faker
from .forms import *
from django.contrib.auth.models import User


fake = Faker()


class AssessmentTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', fake.email(), 'bar')
        self.client.login(username='foo', password='bar')

    def test_Assessment_invalid(self):
        form = AssessmentForm(data={'courseCode': "", 'courseTitle': "data structure", 'assessmentDate': "2020-03-12",
                                    'user': ""})
        self.assertFalse(form.is_valid())

    def test_Assessment_valid(self):
        # user = User.objects.create_user('foo', fake.email(), 'bar')
        self.client.login(username='foo', password='bar')
        form = AssessmentForm(
            data={'courseCode': "CSI247", 'courseTitle': "data structure", 'assessmentDate': "2020-03-12",
                  'user': self.user})
        self.assertTrue(form.is_valid())

    def test_Question_invalid(self):
        data = {''}
        pass

    def test_Question_valid(self):
        pass

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
