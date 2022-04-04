from django.test import TestCase
from django.urls import reverse, resolve
from .models import Post, Comment
from django.contrib.auth import get_user_model
import factory
from faker import Faker, Factory
from factory.django import DjangoModelFactory

User = get_user_model()
faker = Factory.create()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = faker.user_name()
    email = faker.email()

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
    author = factory.SubFactory(UserFactory)
    title = faker.sentence()
    slug = faker.slug()
    content = faker.paragraph()
    status = 'published'
    
class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    author = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    
class PostUpdateTests(TestCase):
    def setUp(self):
        self.post = PostFactory()
        self.updated_title = 'Dummy title'
        url = reverse('blog_handler:post_update', kwargs={'slug': self.post.slug})
        self.client.force_login(self.post.author)
        self.response = self.client.post(url, {'title': self.updated_title})
    
    def test_update_response(self):
        self.assertEqual(self.response.status_code, 200)

class PostCreateTests(TestCase):
    def setUp(self):
        url = reverse('blog_handler:post_create')
        self.user = UserFactory.create()
        self.client.force_login(self.user)
        self.response = self.client.get(url)

    def test_create_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)
