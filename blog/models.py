from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    blog_description = models.TextField(max_length=500, blank=True)
    blog_images = models.ImageField(upload_to='assets/images/blogs/')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('blog_detail', args=[self.blog_title, self.slug])

    def __str__(self):
        return self.blog_title
