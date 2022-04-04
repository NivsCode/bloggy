from django.urls import path
from . import views

app_name = 'blog_handler'
urlpatterns = [
    path('', views.PostPublishedView.as_view(), name='post_published'),
    path('drafts/', views.PostDraftView.as_view(), name='post_drafts'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]