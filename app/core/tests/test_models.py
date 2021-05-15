from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'rob@rob.com'
        password = 'tpasss123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalized_email(self):
        email = 'test@test.com'
        user = get_user_model().objects.create_user(email)
