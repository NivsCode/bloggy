from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpPageView
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def setUp(self):
        self.User = get_user_model()

        def test_create_user(self):
            user = self.User.objects.create_user(
                username='will',
                email='will@example.com',
                password='test@12345'
            )
            self.assertEqual(user.username, 'will')
            self.assertEqual(user.email, 'will@example.com')
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)

        def test_create_superuser(self):
            admin_user = self.User.objects.create_superuser(
                username='will',
                email='will@example.com',
                password='test@12345'
            )
            self.assertEqual(admin_user.username, 'will')
            self.assertEqual(admin_user.email, 'will@example.com')
            self.assertTrue(admin_user.is_staff)
            self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Not on the page')

    def test_signup_form(self):  # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)
