from django.urls import path
from .views import DefaultView, AboutView, ContactView, ResumeView, ServiceView, PortfolioView

urlpatterns = [
    path('', DefaultView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('services/', ServiceView.as_view(), name='services'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    
]