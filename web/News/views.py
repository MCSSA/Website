from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {'time': now})

def about(request):
    return render(request, "about.html", {})