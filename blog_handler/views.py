from django.shortcuts import render
from .models import Post, Comment
from django.views.generics import ListView, DetailView

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'post/post_detail.html'