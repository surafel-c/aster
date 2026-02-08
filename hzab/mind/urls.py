from django.urls import path
from . import views
app_name = "mind"

urlpatterns = [
    path("",views.index,name="index"),
    path("contact/",views.contact,name="contact"),
    path("officials/",views.officials,name="officials"),
    path("organization/",views.organization,name="organization"),
    path("resources/",views.resources,name="resources"),
    path("vacancy/",views.vacancy,name="vacancy"),
    path('news/',views.news,name="news"),
    path('region/',views.region,name="region"),
    path('news/<int:news_id>/',views.full_news,name="full_news"),
]