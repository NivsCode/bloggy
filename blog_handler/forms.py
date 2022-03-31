from .models import Comment, Post
from django.forms import ModelForm, IntegerField

class CommentForm(ModelForm):
    parent_comment_id = IntegerField()
    class Meta:
        model = Comment
        fields = ('content', 'parent_comment_id')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status', )