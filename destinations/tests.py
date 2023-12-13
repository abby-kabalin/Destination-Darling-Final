from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Destination, DestinationComment


# Create your tests here.
class DestinationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
            country="Test Country",
        )

        cls.destination = Destination.objects.create(
            location="TestLocation",
            details="This is a test location",
            country="Tester Country",
            author=cls.user,
        )

    def test_model_content(self):
        self.assertEqual(self.destination.location, "TestLocation")
        self.assertEqual(self.destination.details, "This is a test location")
        self.assertEqual(self.destination.country, "Tester Country")
        self.assertEqual(self.destination.rating, 3)
        self.assertEqual(self.destination.numberReviews, 1)
        self.assertEqual(self.destination.image, "staticfiles/img/dest/no_image.jpg")
        self.assertEqual(self.destination.author.username, "testuser")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_destination_listview(self):
        response = self.client.get(reverse("destination_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test location")
        self.assertTemplateUsed(response, "destination_list.html")

    def test_destination_detailview(self):
        response = self.client.get(
            reverse("destination_detail", kwargs={"pk": self.destination.pk})
        )
        no_response = self.client.get("/destinations/{{self.destination.pk}}/")
        self.assertEqual(no_response.status_code, 404)

    def test_destination_createview(self):
        response = self.client.post(
            reverse("destination_new"),
            {
                "location": "NewLocation",
                "details": "This is a new location",
                "country": "New Country",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Destination.objects.last("location"), "NewLocation")
        self.assertEqual(Destination.objects.last("details"), "This is a new location")
        self.assertEqual(Destination.objects.last("country"), "New Country")
        self.assertEqual(Destination.objects.last("username"), "testuser")

    def test_destination_updateview(self):
        response = self.client.post(
            reverse("destination_edit", args="1"),
            {
                "location": "UpdatedLocation",
                "details": "Updated details about new location",
                "country": "Updated country",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Destination.objects.last("location"), "UpdatedLocation")
        self.assertEqual(
            Destination.objects.last("details"), "Updated details about new location"
        )
        self.assertEqual(Destination.objects.last("country"), "Updated Country")

    def test_destination_deleteview(self):
        response = self.client.post(reverse("destination_delete", args="1"))
        self.assertEqual(response.status_code, 302)


class DestinationCommentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
            country="Test Country",
        )

        cls.destination = Destination.objects.create(
            location="TestLocation",
            details="This is a test location",
            country="Tester Country",
            author=cls.user,
        )

        cls.destinationcomment = DestinationComment.objects.create(
            destination=cls.destination,
            comment="A test comment",
            author=cls.user,
        )

    def test_model_content(self):
        self.assertEqual(self.destinationcomment.destination.pk, "TestLocation")
        self.assertEqual(self.destinationcomment.comment, "A test comment")
        self.assertEqual(self.destination.author.username, "testuser")
