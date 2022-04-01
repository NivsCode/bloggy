from django.shortcuts import render
from django.views.generic import TemplateView
from blog_handler.models import Post

class HomePageView(TemplateView):
	template_name = 'home.html'
	extra_context = {'posts': Post.published.all()}
