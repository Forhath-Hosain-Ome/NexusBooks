from django.views.generic import TemplateView
from core.models import CarosalItem

class HomePage(TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CarosalItem'] = CarosalItem.objects.all()
        return context
