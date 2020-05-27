from django.shortcuts import render
from.models import *

# Create your views here.
def home(request):
    country=Country.objects.all()
    continent=Continent.objects.all()
    context={
        'country':country,
        'continent':continent
    }
    return render(request,'index.html',context)