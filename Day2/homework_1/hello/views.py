from django.shortcuts import render
import hello.views

# Create your views here.

def home(request):
    return render(request, 'home.html')