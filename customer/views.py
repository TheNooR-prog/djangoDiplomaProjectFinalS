from django.shortcuts import render, HttpResponse

# Create your views here.
def customer(request):
    return HttpResponse("Hello from customer")