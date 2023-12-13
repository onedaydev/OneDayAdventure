from django.shortcuts import render


def index(request):    
    return render(request, "index.html")
    

def comingsoon(request):
    return render(request, "comingsoon.html")