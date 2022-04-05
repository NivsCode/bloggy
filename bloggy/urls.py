from django.contrib import admin
from django.urls import path, include
from blog_handler.views import PostPublishedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', PostPublishedView.as_view(), name='home'),
    path('blogs/', include('blog_handler.urls')),
]
