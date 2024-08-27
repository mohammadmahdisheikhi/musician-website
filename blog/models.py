from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
