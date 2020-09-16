from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search/candidates/', views.candidates, name='candidates'),
    path('search/recommendation/', views.recommend, name='recommendation'),
    path('category/', views.category, name='category'),
    path('category/<str:genre>/', views.category_result, name='category_result'),
]