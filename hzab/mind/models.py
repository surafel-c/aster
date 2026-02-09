from django.db import models

# Create your models here.


class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    body  = models.CharField(max_length=1000)
    newsImage = models.ImageField()
    sources = models.CharField(max_length=50)
    
class ContactMessage(models.Model):
    message = models.CharField(max_length=1000)
    email  = models.EmailField(max_length=50)
    name = models.TextField(max_length=100)
    phone = models.CharField(max_length=16)