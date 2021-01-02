from django.urls import path
from .views import *


urlpatterns = [
    # path('/', include("core.urls")),
    path("", IndexView.as_view(), name="index"),
    path("testimonies/", TestimonyView.as_view(), name="testimony"),
    path("vacation/", VacationView.as_view(), name="vacation"),
    path("gallery/", GalleryView.as_view(), name="gallery")

]
