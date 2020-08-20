"""
Included views:

recipe_list: renders the recipes matching the logged in user.
recipe_new: Allows user to create a new recipe
recipe_edit: Allows user to edit recipe
reipc_remove: Allows user to delete recipe
"""
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

@login_required
def recipe_list(request):
    # Show recipes only made by logged-in user.
    recipes = Recipe.objects.filter(author=request.user)

    recipes = recipes.order_by('published_date')
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe_edit.html', {'form': form})

@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/recipe_edit.html', {'form': form})

@login_required
def recipe_remove(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')

# @login_required
# def recipe_detail(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
#     return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
