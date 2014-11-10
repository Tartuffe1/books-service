"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

from userena.models import UserenaSignup

class MyViewTestCase(TestCase):
    def test_login(self):
        my_user = UserenaSignup.objects.create_user(username="my_name", email="my_name@gmail.com", password="my_password")
        active_my_user = UserenaSignup.objects.activate_user(my_user.userena_signup.activation_key)
        log_in = self.client.login(username=active_my_user.username, password="my_password", email= active_my_user.email)
        self.assertEqual(log_in, True)      
