from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_backblaze_b2 import BackblazeB2Storage

class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="", storage=BackblazeB2Storage)  # Assuming you want to store thumbnails as images
    article = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thumbnail.name

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.title


class Popular(models.Model):
    article = models.OneToOneField(BlogArticle, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.article.title} - Views: {self.view_count}"
    
# class UploadedImage(models.Model):
#     image = models.ImageField(upload_to='images/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.image.name
