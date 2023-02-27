from django.db import models
from django.utils import timezone


class NewsletterUser(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    DESIGNERS = [
        ('Ela', 'Ela'),
        ('Lukasz', 'Lukasz')
    ]

    title = models.TextField(max_length=150)
    designer = models.CharField(
        choices=DESIGNERS, max_length=10, default='Ela')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    email = models.ManyToManyField(NewsletterUser, blank=True)
    # add null=True and blank=True to email field
    # Decrease title length to, maybe 254.

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
