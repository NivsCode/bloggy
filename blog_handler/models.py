from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from simple_history.models import HistoricalRecords
from django.contrib.humanize.templatetags.humanize import naturaltime

MAX_TITLE_LENGTH = 200
User = get_user_model()

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class DraftManager(models.Manager):
    def get_queryset(self):
        return super(DraftManager,self).get_queryset().filter(status='draft')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )

    # managers
    objects = models.Manager()
    published = PublishedManager()
    drafts = DraftManager()

    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Version control
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.id} - {self.title} - {self.status} - {self.slug}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse(
            'blog_handler:post_detail',
            args=[self.slug]
        )
    
    def get_history(self):
        version_string = None
        type_dict = {
            '+': 'created',
            '-': 'deleted',
            '~': 'updated'
        }
        version = self.history.latest()
        if version:
            version_string = f'Post was {type_dict[version.history_type]} {naturaltime(version.history_date)}'

        return version_string

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,  related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    # Version control
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.id} - {self.content} - {self.parent_comment}'
    
