from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, BlogPost
from .forms import BlogPostForm, AuthorForm
from datetime import timezone
from django.utils import timezone

def index(request):
    latest_blog_list = BlogPost.objects.order_by('-created_date')[:10]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'posts/index.html', context)

def detail(request, question_id):
    try:
        blogpost = BlogPost.objects.get(pk=question_id)
    except BlogPost.DoesNotExist:
        raise Http404("Blog Post does not exist")
    return render(request, 'posts/detail.html', {'blogpost': blogpost})

# def new(request):
#     form = BlogPostForm()
#     return render(request, 'posts/new.html', {'form': form})


def new(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('/posts/')
    else:
        form = BlogPostForm()
    return render(request, 'posts/new.html', {'form': form})

def new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('/posts/')
    else:
        form = AuthorForm()
    return render(request, 'posts/new_author.html', {'form': form})

