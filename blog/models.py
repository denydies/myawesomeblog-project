from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
