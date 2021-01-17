from django.shortcuts import render
from django.views.generic import TemplateView, View
from core.models import WhatsappInfo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.template import RequestContext


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


class StoreWhatsAppInfo(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        name = request.data.get("name")
        contact = request.data.get("contact")

        if not (name or contact):
            return Response({"message": "please complete all fields"}, status=status.HTTP_400_BAD_REQUEST)

        WhatsappInfo.objects.create(
            name=name,
            phone_number=contact
        )

        return Response({"message": "ok"}, status=status.HTTP_200_OK)


def handler404(request, exception, template_name="page/floral-banner.html"):
    response = render(template_name)
    response.status_code = 404
    return response