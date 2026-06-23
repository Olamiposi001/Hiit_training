from django.urls import path
from projectapp import views
 
urlpatterns = [
    path("", views.home),
    path("about", views.home)
]