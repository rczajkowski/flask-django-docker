from unittest import TestCase
from django.test import Client

class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_add_user_view_get_method(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)

    def test_user_save_method(self):
        from web.forms import UserForm
        form = UserForm(data={'username': 'usernametestss', 'password': 'passwordss'})

        self.assertEqual(form.is_valid(), True)

        response = form.save()
        self.assertEqual(response.status_code, 201)

    def test_show_all_users_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)