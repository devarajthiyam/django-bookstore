from django.http import HttpResponse
from django.views.generic import TemplateView


class ContactUsView(TemplateView):
    template_name = "contact_us.html"


class HomeView(TemplateView):
    template_name = "home.html"


HTML_STRING = """
<h1>Hello World</h1>
"""

def home(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    return HttpResponse(HTML_STRING)