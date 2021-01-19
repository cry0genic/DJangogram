from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView	
from users.forms import CommentForm, PostCreateForm
from users.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.conf import settings

# def home(request):
# 	context = {
# 	'posts': Post.objects.all(),
# 	'title': 'Blog-Home'
# 	}
# 	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'Blog- About'})


class PostListView(ListView): 
	model = Post 
	template_name = 'blog/home.html'
	context_object_name = 'posts' 
	ordering = ['-date_posted'] 
	paginate_by = 5

	

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


def post_detail(request, *args, **kwargs):
	post = get_object_or_404(Post, pk=kwargs.get('pk'))
	comments = Comment.objects.filter(post=post).order_by('-id')

	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(post=post, user=request.user, content=content)
			comment.save()
			return redirect('post-detail', post.id)
	else:
		comment_form = CommentForm()

	context = {
	'post' : post,
	'comments' : comments,
	"comment_form": comment_form
	}
	return render(request, 'blog/post_detail.html', context)


@login_required 
def post_create(request):
	if request.method == "POST":
		form = PostCreateForm(request.POST)
		if form.is_valid():
			title = request.POST.get('title')
			content = request.POST.get('content')
			post = Post.objects.create(title=title, content=content, author=request.user)
			post.save()

			
	else:
		form = PostCreateForm()

	context = {
		'form': form,
	}
	return render(request, 'blog/post_form.html', context)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form): 
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author: 
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/' 

	def test_func(self):
		post = self.get_object() 
		if self.request.user == post.author: 
			return True
		else:
			return False

@login_required
def my_feed(request):
	posts = Post.objects.all()
	profiles = request.user.profile.follows.all()

	context = {
		'posts': posts,
		'profiles': profiles,
	}
	
	return render(request, 'blog/my_feed.html', context)

@login_required
def follow_user(request, *args, **kwargs):
	id = request.POST.get('post_author_profile_id')
	profile = Profile.objects.get(id=id)
	profile.followed_by.add(request.user.profile)

	return redirect('blog-home')

@login_required
def unfollow_user(request, *args, **kwargs):
	id = request.POST.get('post_author_profile_id')
	profile = Profile.objects.get(id=id)
	profile.followed_by.remove(request.user.profile)

	return redirect('blog-home')




# @login_required
# def follow_view(request, id):
#     user_to_follow = get_object_or_404(User, id=id)
#     follower = request.user
#     if follower.profile not in user_to_follow.profile.followers.all():
#         user_to_follow.profile.followers.add(follower.profile)
#         user_to_follow.save()
# 	else:
# 		user_to_follow.profile.followers.remove(follower.profile)
# 		user_to_follow.save()

#     return redirect('blog-home', id=id)








