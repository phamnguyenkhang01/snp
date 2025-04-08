from django.urls import path
from .views import HomePageView, AboutPageView, PostListView, PostDetailView, PostCreateView,\
     PostUpdateView, PostDeleteView, LikePostView, AddCommentView, ProfileUpdateView, friendRequest

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('like/<int:pk>/', LikePostView.as_view(), name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('friend/request/<int:id>/', friendRequest, name='friendRequest'),
]
