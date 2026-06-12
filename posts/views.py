from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post


def home(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

def me(request):
    return HttpResponse("<h1>ITS TEST!</h1>")



def get_posts(request):
    posts = Post.objects.all()  
    categories = Category.objects.filter(is_active=True)  
    
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'posts/post_list.html', context)


def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})