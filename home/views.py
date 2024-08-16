from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


def lock_dashboard(request):
    return render(request, 'pages/lock_dashboard.html')