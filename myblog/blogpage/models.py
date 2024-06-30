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
    cover_image = models.ImageField()
    
    def __str__(self):
        return self.title
    
    