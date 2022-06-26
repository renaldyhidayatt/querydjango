from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from django.utils.text import slugify
from datetime import datetime

# Create your models here.

class Post(models.Model):
    POST_STATUS_CHOICES = (
        ('P', 'Pending for Approval'),
        ('R', 'Rejected'),
        ('A', 'Approved'),
        ('B', 'Blocked')
    )

    title = models.CharField("Post tile", max_length=250, error_messages={
        "max_length": "You cant add more than 250 characters"
    })
    body = models.TextField("Post Description", max_length=5000)
    published_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Post Author")
    category = models.ManyToManyField(Category, blank=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    status = models.CharField(max_length=1, choices=POST_STATUS_CHOICES, default="P")


    class Meat:
        db_table = "Post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        def unique_code():
            return str(datetime.now().timestamp() * pow(10,6))

        
        if not self.slug:
            self.slug = slugify(self.title + unique_code())

        return super().save(*args, **kwargs)