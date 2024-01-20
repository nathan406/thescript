from django.contrib import admin

from .models import BlogArticle,Popular

# Register your models here.

admin.site.register(BlogArticle)
admin.site.register(Popular)