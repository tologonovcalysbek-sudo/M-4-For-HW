from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from .models import Post, Category
from .forms import PostForm, CategoryForm  


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




def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():                          
            form.save()                             
            return redirect('posts')                
    else:

        form = PostForm()             


    return render(request, 'posts/create_post.html', {'form': form})


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = CategoryForm()
        
    return render(request, 'posts/create_category.html', {'form': form})