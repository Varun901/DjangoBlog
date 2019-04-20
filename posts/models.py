from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    created_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

