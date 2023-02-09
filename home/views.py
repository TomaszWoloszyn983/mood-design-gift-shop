from django.shortcuts import render
from .models import NewsletterUser, Post

# Create your views here.

def index(request):
    """ Returns the index page """

    posts = Post.objects.all()
    users = NewsletterUser.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'home/index.html', context)

