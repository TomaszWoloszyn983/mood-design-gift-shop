from django.shortcuts import render, redirect, reverse
from .forms import PostForm
from .models import NewsletterUser, Post

# Create your views here.

def index(request):
    """ Returns the index page """

    posts = Post.objects.all()
    users = NewsletterUser.objects.all()
    template = 'home/index.html'

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Post published 1")
            form = PostForm()
        else: 
            print("\n\n Adding post didn't succeed 1")
    else:
        form = PostForm()

    context = {
        'posts' : posts,
        'form': form
    }
    return render(request, template, context)

