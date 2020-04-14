from django.shortcuts import render

# Create your views here.
def secretary(request):
        return render(request, "secretary/secretary.html")
