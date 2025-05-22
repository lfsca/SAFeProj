from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre/', views.about_view, name='sobre'),
]