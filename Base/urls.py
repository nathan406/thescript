from django.urls import path
from . import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from django.http.response import HttpResponse
import pyrebase

from dotenv import load_dotenv
import os
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='home'),
    path('article/<str:pk>/', views.article, name='article'),
    path('cyber/', views.cyber, name='cyber'),
    path('programming/', views.programming, name='programming'),
    path('tech/', views.tech, name='tech'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
