from django.shortcuts import render
from django.http import HttpResponse
from .models import destination

# Create your views here.

def himakar(request):
    d1 = destination.objects.all()
    return render(request,"index.html",{"d":d1})