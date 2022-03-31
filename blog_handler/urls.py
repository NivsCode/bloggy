from django.urls import path
from . import views

app_name = 'blog_handler'
urlpatterns = [
    path('/drafts', views.PostListView.as_view(), name='post_drafts'),
    path('/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]