from django.test import TestCase, Client
from web.forms import UserForm
class UserFormTest(TestCase):

    def setUp(self):
        self.form = UserForm(data={'username': 'usernametestss', 'password': 'passwordss'})

    def tearDown(self):
        self.client = Client()

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())

    def test_invalid_form(self):
        form = UserForm(data={'email': "", 'password': ""})
        self.assertFalse(form.is_valid())

