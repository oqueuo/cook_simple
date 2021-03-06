"""appmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
    path('recipe/<pk>/remove/', views.recipe_remove, name='recipe_remove'),
    path('recipe/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    # path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]
