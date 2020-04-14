from django.urls import path
from citizen.views import citizen

urlpatterns = [
    path("secretary", citizen, name="secretary"),
]
