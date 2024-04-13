from django.urls import path
from .views import DefaultView, ContactView, ResumeView, ServiceView, PortfolioView
from . import views

urlpatterns = [
    path('', DefaultView.as_view(), name='index'),
    path('about/', views.AboutView, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('services/', ServiceView.as_view(), name='services'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    
]