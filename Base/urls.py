from django.urls import path
from . import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name='home'),
    path('article/<str:pk>', views.article , name='article'),
    path('cyber/', views.cyber , name='cyber'),
    path('programming/', views.programming , name='programming'),
    path('tech/', views.tech , name='tech'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
