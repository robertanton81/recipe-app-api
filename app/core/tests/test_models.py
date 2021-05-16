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
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_super_user_created(self):
        user = get_user_model().objects.create_superuser(
            'mr.rob@emai.com',
            'pass1243'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
