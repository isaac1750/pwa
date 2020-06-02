from django.conf.urls import re_path
from .views import HomePageView, AboutPageView, GalleryPageView
from django.urls import path
from . import views

# wait i will see



urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),

    ]