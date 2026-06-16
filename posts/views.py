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
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Заменили на post.user
            post.rate = 5
            post.save()
            form.save_m2m()
            return redirect('user_posts')
    else:
        form = PostForm()
    
    return render(request, 'posts/create_post.html', {'form': form})


def user_posts(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    posts = Post.objects.filter(user=request.user)  # Заменили на user=request.user
    return render(request, 'posts/user_posts.html', {'posts': posts})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.user != request.user:  # Заменили на post.user
        return HttpResponse("Вы не можете редактировать чужой пост!", status=403)
        
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = PostForm(instance=post)
        
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.user != request.user:  # Заменили на post.user
        return HttpResponse("Вы не можете удалить чужой пост!", status=403)
        
    if request.method == "POST":
        post.delete()
        return redirect('user_posts')
        
    return render(request, 'posts/delete_confirm.html', {'post': post})



def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = CategoryForm()
    
    return render(request, 'posts/create_category.html', {'form': form})