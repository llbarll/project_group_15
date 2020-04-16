from django.shortcuts import render
from users.forms import RegistrationForm
from users.models import Customer
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_customer = Customer()

            # Stock django User model fields
            new_customer.username = data['id_number']
            new_customer.set_password(data['password'])
            new_customer.first_name = data['first_name']
            new_customer.last_name = data['last_name']
            new_customer.email = data['email']

            # Our custom properties
            new_customer.phone_number = data['phone_number']
            new_customer.address = data['address']
            if new_customer.username.endswith('M'):
                new_customer.secretary = True
            else:
                new_customer.citizen = True
            new_customer.save()

            return HttpResponseRedirect(reverse("register_thanks"))
    else:
        form = RegistrationForm()

    return render(request, "users/register.html", {"form": form})


def register_thanks(request):
    return render(request, "users/register_thanks.html")
