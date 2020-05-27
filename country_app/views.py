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

def country(request,cid):
    continent = Continent.objects.all()
    cat = Continent.objects.get(pk=cid)

    country=Country.objects.filter(continent=cat)

    context = {
        'country': country,
        'continent': continent
    }
    return render(request, 'index.html', context)

def details(request,cid):
    country = Country.objects.filter(pk=cid)
    context = {
        'country':country,

    }
    return render(request, 'details.html', context)



