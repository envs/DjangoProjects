from django.test import TestCase, Client
from django.urls import reverse
from main import forms

# Create your tests here.
# One main thing to remember about testing is that you want to test the behaviour 
# rather than the internal implementation

class TestPage(TestCase):

    # Let's test the behavior at HTTP level rather than at the browser level
    # We want to make sure that The HTTP status code is 200, The template home.html 
    # has been used, and the Response contains the name of our shop
    def test_home_page_works(self):
        #self.client = Client()
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')
        # response = self.client.get("/")
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'home.html')
        # self.assertContains(response, 'BookTime')


    def test_about_us_page_works(self):
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, 'BookTime')


    def test_contact_us_page_works(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')
        self.assertContains(response, 'BookTime')
        self.assertIsInstance(
            response.context["form"], forms.ContactForm
        )