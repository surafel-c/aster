from django.db import models

# Create your models here.


class News(models.Model):
    news_id = models.IntegerField(max_length=2000 ,primary_key=True)
    title = models.CharField(max_length=20)
    body  = models.CharField(max_length=1000)
    newsImage = models.ImageField()
    sources = models.CharField(max_length=50)
    
    