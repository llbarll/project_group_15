from django.urls import path
from citizen.views import citizen

urlpatterns = [
    path("citizen", citizen, name="citizen"),
]
