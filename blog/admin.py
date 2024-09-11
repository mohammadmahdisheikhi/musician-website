from django.contrib import admin
from .models import BlogPost, Video

admin.site.register(BlogPost)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']