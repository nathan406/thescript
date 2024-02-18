
from django.contrib import admin
from django.urls import path
from django.urls import include
from Base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls')),
    
    # path('', views.upload_image_to_firebase, name='upload') 
]
