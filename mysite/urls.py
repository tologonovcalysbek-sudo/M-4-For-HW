"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posts.views import (
    HomeView,
    AboutView,
    MeView,
    PostListView,
    PostDetailView,
    PostCreateView,
    UserPostListView,
    PostUpdateView,
    PostDeleteView,
    CategoryCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("test/", MeView.as_view(), name="test"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/detail/", PostDetailView.as_view(), name="post_detail"),
    path("posts/create/", PostCreateView.as_view(), name="create_post"),
    path("category/create/", CategoryCreateView.as_view(), name="create_category"),
    path("posts/my/", UserPostListView.as_view(), name="user_posts"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="edit_post"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)