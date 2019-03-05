
from django.contrib import admin
from django.urls import path, include 
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('algo/', views.fetch, name='fetch'),
    path('', views.index),



]
