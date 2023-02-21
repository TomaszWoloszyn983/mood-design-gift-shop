from django import forms
from .models import NewsletterUser, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title", "designer", "body", "image", "email"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        users = NewsletterUser.objects.all()


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = (
            "email",
        )
