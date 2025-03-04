from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from accounts.models import CustomUser
from accounts.forms import CustomUserChangeForm
from .models import Post

from django.http import JsonResponse
from django.views import View
from .models import Post, Like, Comment

from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
def homePageView(request):
    return HttpResponse("Hello world")

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ProfileUpdateView(UpdateView):
    model = CustomUser
    form = CustomUserChangeForm
    template_name = 'user_update.html'
    fields = ['mobile', 'email', 'avatar', 'first_name', 'last_name', 'bio', 'dob', 'gender']
    
    success_url=reverse_lazy('posts')

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch comments sorted by created_at in descending order
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-created_at')
        return context

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
    
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        text = request.POST.get("text", "").strip()

        if not text:
            return JsonResponse({"error": "Comment cannot be empty"}, status=400)

        comment = Comment.objects.create(post=post, user=request.user, text=text)

        return JsonResponse({
            "id": comment.id,
            "user": comment.user.username,
            "text": comment.text,
            "created_at": comment.created_at.strftime('%Y-%m-%d %H:%M')
        })
