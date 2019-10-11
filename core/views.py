from django.shortcuts import render
import redis

# Create your views here.

def home (request):
    r = redis.Redis('localhost')
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')