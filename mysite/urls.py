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

from posts.views import about, get_post, get_posts, home, me

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("test/", me, name="test"),
    path("posts/", get_posts, name="posts"),
    path("post/<int:pk>/detail/", get_post, name="post_detail"),
]
































# from django.db import models




# class Category(models.Model):
#     name = models.CharField()


# class Post(models.Model):
#     title = models.CharField()
#     content = models.TextField()
#     rate = models.IntegerField()
#     user = models.CharField(max_length=255, null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL)

# ulpaterns = [
#     path('admin/', admin.site.urls),
#     path('',category_list),
#     path('categoryies/',category_list),
# ]
























# C-R-U-D

# C - create
# INSERT INTO (fields) VALUES (values);
# Model.objects.create(name='asdasd', rate=2)
# user = User(name="islam", age=22)
# user.save()

# R - read
# SELECT * FROM table_name WHERE id=1;
# users = User.objects.all()


# U - update
# UPDATE table_name SET field_name=value;
# user = User.objects.get(name="islam")
# user.name = "Islam"
# user.save()

# D - delete
# DELETE table_name WHERE id=1;
# user = User.objects.get(name="islam")
# user.delete()