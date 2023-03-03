from django.contrib import admin
from .models import NewsletterUser, Post


class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'added_on',
    )

    ordering = ('-added_on',)


admin.site.register(NewsletterUser)
admin.site.register(Post)
