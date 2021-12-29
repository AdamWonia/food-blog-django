from django.db import models
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="post author")
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)
    published_date = models.DateTimeField(default=now)
    image = models.ImageField(blank=True, null=True, upload_to='image/', default='image/white_img.png')

    def publish(self):
        self.published_date = now
        self.save()

    def __str__(self):
        return self.title
