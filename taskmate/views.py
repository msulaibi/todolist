from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "home":"Welcome to Home Page",
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        "about":"Welcome to About Page",
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        "contact":"Welcome to Contact Page",
    }
    return render(request, 'contact.html', context)