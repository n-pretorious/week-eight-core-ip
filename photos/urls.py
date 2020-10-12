from os import pathconf
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.index, name='allPhotos'),
    path('categories/', views.categories, name='category-list'),
    path('locations/', views.locations, name='location-list'),
    path('category/images/<int:category_name>',
         views.category_view, name='by_category'),
    path('location/images/<int:place>', views.location_view, name='by_location'),
    path('search-results/', views.search, name='image-search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
