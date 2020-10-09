from django.shortcuts import render

# Create your views here.

def allPhotos(request):
    return render(request, "index.html")