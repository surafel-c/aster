from django.contrib import admin

# Register your models here.
from .models import News,ContactMessage

admin.site.register(News)
admin.site.register(ContactMessage)
