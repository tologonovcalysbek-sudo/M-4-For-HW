from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category
from .forms import PostForm, CategoryForm

class HomeView(TemplateView):
    template_name = "base.html"

class AboutView(TemplateView):
    template_name = "about.html"

class MeView(View):
    def get(self, request):
        return HttpResponse("<h1>ITS TEST!</h1>")

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('user_posts')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.rate = 5
        return super().form_valid(form)

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    login_url = 'home'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('user_posts')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            return HttpResponseForbidden("Вы не можете редактировать чужой пост!")
        return super().dispatch(request, *args, **kwargs)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_confirm.html'
    success_url = reverse_lazy('user_posts')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            return HttpResponseForbidden("Вы не можете удалить чужой пост!")
        return super().dispatch(request, *args, **kwargs)

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'posts/create_category.html'
    success_url = reverse_lazy('user_posts')