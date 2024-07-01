from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200, default="anonymous")
    contents = CKEditor5Field()
    tags = models.CharField(max_length=200)
    is_popular = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='media/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    