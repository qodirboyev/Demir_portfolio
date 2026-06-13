from django.db import models
from django.urls import reverse
# Create your models here.


class Family_blog(models.Model):
    image = models.ImageField(upload_to='media/family_foto')
    title = models.CharField(max_length=150)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('family')



class Logo(models.Model):
    image = models.ImageField(upload_to='media/logo')
    title = models.CharField(max_length=150)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('logo')