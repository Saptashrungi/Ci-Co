from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.Login, name ='login'),
    path('/', views.Logout, name ='logout'),
    path('register/', views.register, name ='register'),
    path('check/', views.check, name ='check'),
]
