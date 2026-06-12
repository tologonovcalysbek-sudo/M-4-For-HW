from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Category  

from posts.models import Post


def home(request):
    return render(request, "base.html")


def about(request):

    return render(request, "about.html")


def me(request):

    return HttpResponse("<h1>ITS TEST!</h1>")


def post(request):
    posts = Post.objects.all()

    text = ""

    for post in posts:
        text += f"<h1>{post.title}</h1> <br> {post.content}<br>"

    return HttpResponse(text)


def get_posts(request):
    posts = Post.objects.all()

    return render(request, "posts/post_list.html", context={"posts": posts})


def get_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "posts/post_detail.html", context={"post": post})







def active_categories_view(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'posts/category_list.html', {'categories': categories})