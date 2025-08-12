from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blog/videos/', views.video_list, name='video_list'),
    path('blog/gallery/', views.photo_gallery, name='photo_gallery'),
]  

