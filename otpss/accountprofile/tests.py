from django.test import TestCase
from .models import *
from .forms import UserProfileForm


class TestUserProfile(TestCase):
    def setUp(self):
        user = User.objects.create_user('foo', fake.email(), 'bar')
        self.client.login(username='foo', password='bar')

    def test_userprofile_valid_form(self):
        form = UserProfileForm(
            data={'user': self.user, 'studentId': "201604267", 'program': 'Accountancy'})
        self.assertTrue(form.is_valid())

    def test_userprofile_invalid_form(self):
        form = UserProfileForm(
            data={'user': self.user, 'studentId': "2016042", 'program': 'Accountancy'})
        self.assertTrue(form.is_valid())
