from django.http import HttpResponse
from django.shortcuts import render
from .models import News,ContactMessage


def index(request):
    return render(request, 'mind/index.html')

def resources(request):
    return render(request,"mind/resources.html")

# def contact(request):
#     return render(request, 'mind/contact.html')

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




# views.py
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        # Access form fields
        name = request.POST.get("name", "").strip()      # empty string fallback
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        phone = request.POST.get("phone", "").strip()
        

        # Simple validation
        errors = []
        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        if not message:
            errors.append("Message is required.")
        if not phone:
            errors.append("add phone number.")

        if errors:
            # Re-render form with errors
            return render(request, "mind/contact.html", {"errors": errors,
                                                    "name": name,
                                                    "email": email,
                                                    "message": message})

        # Handle the data (e.g., save to DB or send email)
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message,
            phone=phone,
        )
        return render(request, "mind/contact.html",{"succes":"your form is submited."})

    # GET request → render empty form
    return render(request, "mind/contact.html")
