from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Comment, Follow, Group, Post, User
from .utils import pagination


def index(request):
    posts = pagination(Post.objects.all(), request)
    return render(request, 'posts/index.html', posts)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group
    }
    context.update(pagination(posts, request))
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    following = request.user.is_authenticated and Follow.objects.filter(
        user=request.user, author=author
    ).exists()
    context = {
        'author': author,
        'following': following
    }
    context.update(pagination(author.posts.all(), request))
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    form = CommentForm(request.POST or None)
    context = {
        'posts': post,
        'form': form,
        'comments': comments
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    is_edit = False
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=post.author)
    return render(request, 'posts/create_post.html', {
        'form': form, 'is_edit': is_edit
    }
    )


@login_required
def post_edit(request, post_id):
    is_edit = True
    user = request.user
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None,
                    files=request.FILES or None,
                    instance=post)
    context = {
        'post': post,
        'form': form,
        'is_edit': is_edit
    }
    if user != post.author:
        return redirect('post:post_detail', post.pk)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post.pk)
    return render(request, 'posts/create_post.html', context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    else:
        return render(request, 'posts/includes/comment.html', {'form': form})
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def follow_index(request):
    following = Post.objects.filter(
        author__following__user=request.user)
    context = {}
    context.update(pagination(following, request))
    return render(request, 'posts/follow.html', context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if request.user != author:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('posts:profile', author)


@login_required
def profile_unfollow(request, username):
    user = get_object_or_404(User, username=username)
    Follow.objects.filter(user=request.user, author=user).delete()
    return redirect('posts:profile', user)
