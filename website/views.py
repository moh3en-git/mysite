from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request,'website\index.html')

def home_contact(request):
    return render(request,'website\contact.html')

def home_about(request):
    return render(request,'website\\about.html')