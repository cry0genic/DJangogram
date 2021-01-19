from django.urls import path
from .views import PostListView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'), 
	path('post/<int:pk>/', views.post_detail, name='post-detail'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('post/new/', views.post_create, name='post-create'),
	path('about/', views.about, name='blog-about'),
	path('follow-user/', views.follow_user, name='follow-user'),
	path('unfollow-user/', views.unfollow_user, name='unfollow-user'),
	path('my-feed/', views.my_feed, name='my-feed'),
	
]