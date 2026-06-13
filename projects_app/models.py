from django.db import models
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    url = models.URLField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects')