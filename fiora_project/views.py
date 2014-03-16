from accounts.forms import IamaForm 
from django.views.generic import TemplateView
from random import randint
from theme import Theme
class HomeView(TemplateView):
    template_name="index.html"
    
    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        theme = Theme.get_random_theme()
        context['banner_class'] = theme.css_class
        context['iama_form'] = IamaForm(initial={'weapon':theme.weapon, 'gender':theme.gender})
        return context