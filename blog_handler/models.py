from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse

MAX_TITLE_LENGTH = 200
User = get_user_model()

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    slug = models.SlugField()
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.title} - {self.status} - {self.slug}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('posts')

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.content}'
    