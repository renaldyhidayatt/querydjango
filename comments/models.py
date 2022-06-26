from django.db import models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commented_by = models.CharField(max_length=150)

    class Meta:
        db_table = "Comment"
        verbose_name = "Comment"
        verbose_name_plural = 'Comments'

    def __str__(self) -> str:
        return self.body