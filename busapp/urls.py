from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('Projects/', views.Projects, name='Projects'),
    path('certification/',views.certification,name='certification'),
    path('contact/', views.contact, name='contact'),
]
