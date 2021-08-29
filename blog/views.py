from django.shortcuts import render, get_object_or_404
from .models import Posts


def show_blog(request):
    posts = Posts.objects
    return render(request, 'blog/blog.html', {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'blog/show_post.html', {'post': post})
