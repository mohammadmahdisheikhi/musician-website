from django.contrib import admin
from .models import BlogPost, Video, Photo

admin.site.register(BlogPost)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']