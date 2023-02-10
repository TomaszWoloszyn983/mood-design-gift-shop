from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import PostForm, NewsletterForm
from .models import NewsletterUser, Post
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail



def index(request):
    """ Returns the index page """

    posts = Post.objects.all()
    users = NewsletterUser.objects.all()
    template = 'home/index.html'
    newsletterForm = NewsletterForm()

    if request.method == 'POST':
        print('\nHeloo from index')
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
        'form': form,
        'newsletterForm': newsletterForm
    }
    return render(request, template, context)


def send_post(request):
    """
    Sents a post taken from post form
    Publishes the post on the Home Page.
    Displays refreshed Home Page.

    Sents the posts content to Newsletter Users
    """
    posts = Post.objects.all()
    users = NewsletterUser.objects.all()
    newsletterForm = NewsletterForm()

    if request.method == 'POST':
        print('\nHeloo from send post')
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post successfully published')

            # send the post to newsletter users
            post_title = form.cleaned_data.get('title')
            post_content = form.cleaned_data.get('body')
            marked_emails = form.cleaned_data.get('email')

            for user in marked_emails:
                print(f'Sending post {post_title} to {user}')
                send_newsletter(user, post_title, post_content)

            form = PostForm()
        else: 
            messages.success(request, f'Adding post did not succeed')
    else:
        form = PostForm()
    
    context = {
        'posts' : posts,
        'form': form,
        'newsletterForm': newsletterForm
    }
    return render(request, 'home/index.html', context)



def newsletter(request):
    """
    Sents a post taken from post form
    Publishes the post on the Home Page.
    Displays refreshed Home Page.
    """
    # I'm not sure if all this is needed here
    posts = Post.objects.all()
    users = NewsletterUser.objects.all()
    newsletterForm = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        user = NewsletterUser(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get('email')
            form.save()
            messages.success(request, f'Thank you. \nNewsletter sent to: {user_email}')

            # Sending welcome message
            subject = "Mood Designs Newsletter"
            content = """Thank you for your subscription
                \nNow you will be always up to date
                with the latest
                \nevents, promotion and our new products
                \n\n   Kind regards Ela nad Lukasz."""
            send_newsletter(user_email, subject, content)
            form = NewsletterForm()
        else: 
            messages.error(request, f'I could not register this user.')
    else:
        form = NewsletterForm()

    context = {
        'posts' : posts,
        'form': form,
        'newsletterForm': newsletterForm
    }
    return render(request, 'home/index.html', context)



def send_newsletter(email, subject, content):
    """
    Send subscription email information to Newsletter Users
    Takes as arguments:
    Users email address.  Email subject and email content.
    """
    cust_email = email

    send_mail(
        subject,
        content,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
