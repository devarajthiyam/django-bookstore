from django.views.generic import TemplateView

class ContactUsView(TemplateView):
    template_name = "contact_us.html"



class HomeView(TemplateView):
    template_name = "home.html"