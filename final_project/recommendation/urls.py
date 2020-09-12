from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('select/search', views.search, name='search'),
    path('select/search/result', views.search_result, name='search_result'),
    path('select/category/', views.category, name='category'),
    path('select/category/result', views.category_result, name='category_result'),
]