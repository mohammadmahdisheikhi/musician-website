from django.shortcuts import get_object_or_404, render
from .models import BlogPost, Video, Photo

def blog_list(request):
    blogs = BlogPost.objects.all()  # Fetch all blog posts from the database
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog/blog.html', {'blog': blog})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'blog/videos.html', {'videos': videos})

def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'blog/photos.html', {'photos': photos})