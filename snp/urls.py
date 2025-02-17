from django.urls import path
from .views import HomePageView, AboutPageView, PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
]
