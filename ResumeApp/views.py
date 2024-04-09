from django.views.generic import TemplateView

# Create your views here.
class DefaultView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ResumeView(TemplateView):
    template_name = 'resume.html'

class ServiceView(TemplateView):
    template_name = 'services.html'

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'