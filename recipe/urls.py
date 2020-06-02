from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
    path('recipe/<pk>/remove/', views.recipe_remove, name='recipe_remove'),
    path('recipe/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipe/', views.eats, name='eats')
]