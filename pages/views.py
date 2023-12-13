from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get", "post"]


class AboutPageView(TemplateView):
    template_name = "findOutMore.html"
    http_method_names = ["get", "post"]
