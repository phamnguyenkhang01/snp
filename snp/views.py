from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post

# Create your views here.
def homePageView(request):
    return HttpResponse("Hello world")

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    def get_queryset(self):
        # Order posts by 'date_time' in descending order (newest posts first)
        return Post.objects.all().order_by('-date_time')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['text', 'img', 'author']



    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['text', 'img']
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')