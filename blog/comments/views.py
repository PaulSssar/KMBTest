from django.shortcuts import render, get_object_or_404
from posts.models import Post
from .models import Comment
from .forms import CommentForm


def comments_list(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'comments.html', context)
