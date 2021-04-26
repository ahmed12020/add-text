from django.test import TestCase

# Create your tests here.
class SchoolTest(TestCase):
    def btn(self):
        response = self.client.get('/prof/')
        self.assertEqual(response.status_code, 200)