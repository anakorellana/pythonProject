from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django .urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    snippet = models.TextField(default="Read More")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default="default.jpeg", upload_to="photos/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="no-image.jpg")
    success_url = reverse_lazy('blog-home')

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.post.title, self.name)
