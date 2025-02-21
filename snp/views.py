from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post

from django.http import JsonResponse
from django.views import View
from .models import Post, Like

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
    
class LikePostView(View):
    def post(self, request, pk):
        # Fetch the post object using the primary key
        post = Post.objects.get(pk=pk)
        
        # Check if the user has already liked the post (optional, you can prevent double likes)
        user = request.user
        if Like.objects.filter(post=post, user=user).exists():
            return JsonResponse({'error': 'You have already liked this post'}, status=400)
        
        # Create a new Like entry
        Like.objects.create(post=post, user=user)
        
        # Get the updated like count for the post
        like_count = post.likes.count()
        
        # Return the updated like count as JSON
        return JsonResponse({'like_count': like_count})