from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpPageView


class SignUpPageTests(TestCase):
	def setUp(self):
		url = reverse('signup')
		self.response = self.client.get(url)

	def test_signup_template(self):
		self.assertEqual(self.response.status_code, 200)
		self.assertTemplateUsed(self.response, 'registration/signup.html')
		self.assertContains(self.response, 'Sign Up')
		self.assertNotContains(self.response, 'Not on the page')

	def test_signup_form(self): # new 
		form = self.response.context.get('form')
		self.assertIsInstance(form, CustomUserCreationForm)
		self.assertContains(self.response, 'csrfmiddlewaretoken') 
	
	def test_signup_view(self):
		view = resolve('/accounts/signup/')
		self.assertEqual( view.func.__name__, SignUpPageView.as_view().__name__ )