import pyperclip
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Location, Category

def index(request):

  all_images = Image.objects.order_by('-id').all()

  context = {
    'images':all_images
  }
  return render(request, 'photos/index.html', context)


def categories(request):

  title = 'Categories'

  all_categories = Category.objects.all()
  context = {
    'categories':all_categories,
    'title': title
  }
  return render(request, 'photos/categories.html', context)


def locations(request):

  title = 'Locations'

  all_locations = Location.objects.all()

  context = {
    'locations':all_locations,
    'title': title
  }

  return render(request, 'photos/locations.html', context)


def categoryView(request, category_name):

  cat = Image.by_category(category_name)

  context = {
    'cat_results': cat
  }

  return render(request, 'photos/categoryView.html', context)


def locationView(request, place):

  locale = Image.by_location(place)

  context = {
    'loc_results': locale,
  }

  return render(request, 'photos/locationView.html', context)


def search(request):
  query = request.GET.get('q')
  results = Image.objects.filter(
    Q(category__cat_name__icontains=query)  
    )  
  context ={
    'results':results,
    'term':query
  }
  return render(request, 'photos/search.html', context)