from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search/candidates/', views.candidates, name='candidates'),
    path('search/recommendation/', views.recommendation, name='recommendation'),
    path('category/', views.category, name='category'),
    path('category/result/', views.category_result, name='category_result'),
]