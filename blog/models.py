import uuid
from django.db import models
# from ckeditor.fields import RichTextField

from django.utils.text import slugify
from django.db.models.signals import pre_save

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images/')
    slug = models.SlugField(unique=True)
    content = models.TextField('Content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.title:
                self.slug = slugify(self.title)
            else:
                self.slug = uuid.uuid4().hex[:8]  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or str(self.id) 
