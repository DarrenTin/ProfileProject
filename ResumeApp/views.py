from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Identity, Level, Fact

# Create your views here.
class DefaultView(TemplateView):
    template_name = 'index.html'

# class AboutView(ListView):
#     model = Identity
#     context_object_name = 'identity_list'
#     template_name = 'about.html'

def AboutView(request):
    identity_list = Identity.objects.all()
    level_list = Level.objects.all()
    fact_list = Fact.objects.all()
    context = {'identity_list': identity_list, 'level_list': level_list, 'fact_list': fact_list}
    return render(request, 'about.html', context)

class ContactView(TemplateView):
    template_name = 'contact.html'

class ResumeView(TemplateView):
    template_name = 'resume.html'

class ServiceView(TemplateView):
    template_name = 'services.html'

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'