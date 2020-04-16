from django.shortcuts import render

# Create your views here.
def citizen(request):
        return render(request, "citizen/citizen.html")
