from django import forms
from .models import BlogPost, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "bio")


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "description", 'author')



