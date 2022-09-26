from django.shortcuts import render

# Create your views here.
from pickletools import read_uint1
from django.http import HttpResponse

from apiproject.models import Contact




def index(request):
    if request.method == "POST":
        name = request.POST.get('inputName');
        email = request.POST.get('inputEmail');
        phone = request.POST.get('inputPhone');
        city = request.POST.get('inputCity');
        state = request.POST.get('inputState');
        country = request.POST.get('inputCountry');

        print(name);

        contact = Contact( name=name,email=email, phone=phone , city=city , state=state , country=country)
        contact.save()
    return render(request,'index.html')