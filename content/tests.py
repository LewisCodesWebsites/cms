from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import ContentItem

class ContentItemTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="testpass")

    def test_create_and_view_item(self):
        self.client.login(username="alice", password="testpass")
        item = ContentItem.objects.create(title="Hello", body="World", created_by=self.user)
        response = self.client.get(reverse("content_detail", args=[item.pk]))
        self.assertContains(response, "Hello")
        self.assertContains(response, "World")


    def test_accounts_login_page(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
