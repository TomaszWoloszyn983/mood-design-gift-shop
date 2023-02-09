from django import forms
from .models import NewsletterUser, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title", "designer", "body", "image", "email"
        )

    # title = models.TextField()
    # designer = models.CharField(choices=DESIGNERS, max_length=10, default='Ela')
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)
    # body = models.TextField()
    # image = models.ImageField(null=True, blank=True)
    # email = models.ManyToManyField(NewsletterUser)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        users = NewsletterUser.objects.all()

        # self.fields['category'].choices = friendly_names

        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'border-black rounded-0'
