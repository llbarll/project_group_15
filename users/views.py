from django.shortcuts import render
from users.forms import RegistrationForm,LoginForm
from users.models import Customer
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse



# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_customer = Customer()
            #Check if id_number has more than 8 characters
            # if it has only 8 , so its a regular user
            # if it has 9 , then check the last charaacter
            # if its 'A' then it should be is_superuser= true
            # if its 'M' then it should be is_staff =true
            
            # Stock django User model fields
            new_customer.username = data['id_number']
            new_customer.set_password(data['password'])
            new_customer.first_name = data['first_name']
            new_customer.last_name = data['last_name']
            new_customer.email = data['email']
            if len(data['id_number']) > 8:
                if data['id_number'][len(data['id_number'])-1] == 'A':
                    new_customer.is_superuser = True
                if  data['id_number'][len(data['id_number'])-1] == 'M':
                    new_customer.is_staff = True
             

            # Our custom properties
            new_customer.phone_number = data['phone_number']
            new_customer.address = data['address']

            new_customer.save()

            return HttpResponseRedirect(reverse("register_thanks"))
    else:
        form = RegistrationForm()

    return render(request, "users/register.html", {"form": form})


def register_thanks(request):
    return render(request, "users/register_thanks.html")

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            userLoggedIn = Customer.objects.filter(Q(username=data["id_number"])|Q(password=data["password"]))
            if userLoggedIn.exists():
                request.session["loggedUser"] = userLoggedIn.values('first_name')[0].get('first_name')
                if userLoggedIn.values('is_staff')[0].get('is_staff') == True:
                    request.session["loggedUserRole"]="secretary"
                    return render(request,"secretary/secretary.html")
                else:
                    request.session["loggedUserRole"]="citizen"
                    return render(request,"citizen/citizen.html")
    else:
        form = LoginForm()
        
    return render(request,"users/login.html", {"form":form})

        
    