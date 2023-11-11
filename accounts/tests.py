from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
            country="testPlace",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.country, "testPlace")
        self.assertEqual(user.status, "Egg")
        self.assertEqual(user.numContributions, 0)

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
            country="testPlace",
        )
        self.assertEqual(user.username, "testsuperuser")
        self.assertEqual(user.email, "testsuperuser@example.com")
        self.assertEqual(user.country, "testPlace")
        self.assertEqual(user.status, "Egg")
        self.assertEqual(user.numContributions, 0)

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        
