from django.http import HttpResponse
from django.shortcuts import render
from .models import News


def index(request):
    return render(request, 'mind/index.html')

def resources(request):
    return render(request,"mind/resources.html")

def contact(request):
    return render(request, 'mind/contact.html')

def vacancy(request):
    return render(request,"mind/vacancy.html")

def resources(request):
    return render(request, 'mind/resources.html')

def officials(request):
    return render(request,"mind/officials.html")

def news(request):
    return render(request, 'mind/news.html')

def organization(request):
    return render(request,"mind/organizational.html")
def region(request):
    return render(request,'mind/region.html')
def full_news(request,news_id):
    my_news = News.objects.get(news_id=news_id)
    return render(request,"mind/full_news.html",{"my_news":my_news})