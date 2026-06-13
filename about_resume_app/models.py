from django.db import models
from django.urls import reverse
# Create your models here.


class Resume(models.Model):
    kasb = models.CharField(max_length=200)
    about = models.TextField()
    dev_long = models.CharField(max_length=200)
    frameworks = models.CharField(max_length=200)
    database = models.CharField(max_length=200)
    frontend_t = models.CharField(max_length=200)
    python_modul = models.CharField(max_length=200)
    ish_joy = models.CharField(max_length=200)
    lavozim = models.CharField(max_length=200)
    vazifalar = models.CharField(max_length=200)
    ishlash_davri = models.CharField(max_length=200)
    yutuq_rasm = models.ImageField(upload_to='media/photos')
    yutuq_info = models.CharField(max_length=200)
    life_long = models.CharField(max_length=200)
    def __str__(self):
        return self.kasb

    def get_absolute_url(self):
        return reverse('resume')




class About_blog(models.Model):
    image = models.ImageField(upload_to='media/photos')
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about')