from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post
from .forms import PostForm


def posts_list(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'posts.html', context)
