from django.db import models
from django.utils import timezone
from django.db.models import Model
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=True, null=True)
    name = models.CharField(max_length=255, default="Some String")


class Post(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_image/')

    def str(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
