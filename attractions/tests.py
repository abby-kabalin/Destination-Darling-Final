from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Attraction, AttractionComment


# Create your tests here.
class AttractionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
            country="Test Country",
        )

        cls.attraction = Attraction.objects.create(
            name="TestLocation",
            description="This is a test location",
            address="Somewhere, Somplace",
            author=cls.user,
        )

    def test_model_content(self):
        self.assertEqual(self.attraction.name, "TestLocation")
        self.assertEqual(self.attraction.description, "This is a test location")
        self.assertEqual(self.attraction.address, "Tester Country")
        self.assertEqual(self.attraction.image, "staticfiles/img/dest/no_image.jpg")
        self.assertEqual(self.attraction.author.username, "testuser")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_attraction_listview(self):
        response = self.client.get(reverse("attraction_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test location")
        self.assertTemplateUsed(response, "attraction_list.html")

    def test_attraction_detailview(self):
        response = self.client.get(
            reverse("attraction_detail", kwargs={"pk": self.attraction.pk})
        )
        no_response = self.client.get("/attractions/{{self.attraction.pk}}/")
        self.assertEqual(no_response.status_code, 404)

    def test_attraction_createview(self):
        response = self.client.post(
            reverse("attraction_new"),
            {
                "name": "NewLocation",
                "description": "This is a new location",
                "address": "New Country",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Attraction.objects.last("name"), "NewLocation")
        self.assertEqual(
            Attraction.objects.last("description"), "This is a new location"
        )
        self.assertEqual(Attraction.objects.last("address"), "New Country")
        self.assertEqual(Attraction.objects.last("username"), "testuser")

    def test_attraction_updateview(self):
        response = self.client.post(
            reverse("attraction_edit", args="1"),
            {
                "name": "UpdatedLocation",
                "description": "Updated details about new location",
                "address": "Updated country",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Attraction.objects.last("name"), "UpdatedLocation")
        self.assertEqual(
            Attraction.objects.last("description"), "Updated details about new location"
        )
        self.assertEqual(Attraction.objects.last("address"), "Updated Country")

    def test_attraction_deleteview(self):
        response = self.client.post(reverse("attraction_delete", args="1"))
        self.assertEqual(response.status_code, 302)


class AttractionCommentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
            country="Test Country",
        )

        cls.attraction = Attraction.objects.create(
            name="TestLocation",
            description="This is a test location",
            address="Tester Country",
            author=cls.user,
        )

        cls.attractioncomment = AttractionComment.objects.create(
            attraction=cls.attraction,
            comment="A test comment",
            author=cls.user,
        )

    def test_model_content(self):
        self.assertEqual(self.attractioncomment.attraction.pk, "TestLocation")
        self.assertEqual(self.attractioncomment.comment, "A test comment")
        self.assertEqual(self.attraction.author.username, "testuser")
