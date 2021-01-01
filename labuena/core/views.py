from django.shortcuts import render
from django.views.generic import TemplateView, View


# Create your views here.

class IndexView(View):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, dict())


class TestimonyView(View):

    template_name = "testimonies/index.html"

    def get(self, request, *args, **kwargs):
        print("inside testimony video")
        return render(request, self.template_name, dict())


class VacationView(View):

    template_name = "vacations/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, dict())


class GalleryView(View):
    template_name = "gallery/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, dict())
