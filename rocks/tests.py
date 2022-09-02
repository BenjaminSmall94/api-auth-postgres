from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Rock


class RockTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_rock = Rock.objects.create(
            name="Fork",
            owner=testuser1,
            description="Better than a spoon except for soup.",
        )
        test_rock.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_rocks_model(self):
        rock = Rock.objects.get(id=1)
        actual_owner = str(rock.owner)
        actual_name = str(rock.name)
        actual_description = str(rock.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Fork")
        self.assertEqual(
            actual_description, "Better than a spoon except for soup."
        )

    def test_get_rock_list(self):
        url = reverse("rock_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        rocks = response.data
        self.assertEqual(len(rocks), 1)
        self.assertEqual(rocks[0]["name"], "Fork")

    def test_get_rock_by_id(self):
        url = reverse("rock_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        rock = response.data
        self.assertEqual(rock["name"], "Fork")

    def test_create_rock(self):
        url = reverse("rock_create")
        data = {"owner": 1, "name": "limestone", "description": "hard rock cafe"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        rocks = Rock.objects.all()
        self.assertEqual(len(rocks), 2)
        self.assertEqual(Rock.objects.get(id=2).name, "limestone")

    def test_update_rocks(self):
        url = reverse("rock_update", args=(1,))
        data = {
            "owner": 1,
            "name": "Fork",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        rock = Rock.objects.get(id=1)
        self.assertEqual(rock.name, data["name"])
        self.assertEqual(rock.owner.id, data["owner"])
        self.assertEqual(rock.description, data["description"])

    def test_delete_rock(self):
        url = reverse("rock_delete", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        rocks = Rock.objects.all()
        self.assertEqual(len(rocks), 0)
