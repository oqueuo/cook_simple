from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Recipe
from .forms import RecipeForm
import json
from django.http import HttpResponse


@login_required
def recipe_list(request):
    # Show recipes only made by logged-in user.
    recipes = Recipe.objects.filter(author=request.user)

    recipes = recipes.order_by('published_date')
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})

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

# def eats(request):
#     # 1. Open csv and load it into a df
#     # 2. Use the query from the request to filter the df for only the recipe we want
#     # 3. Return the json.
#     data = {'name': 'Instant Pot® Chicken Paprikash',
#             'time':{'Prep': '15 m', 'Cook': '40 m', 'Ready In': '1 h 10 m'},
#             'ingredients':['1 (12 ounce) package egg noodles', '2 tablespoons butter', '1 tablespoon minced parsley', '1 1/2 teaspoons salt, divided', '1 teaspoon ground black pepper, divided', '1 tablespoon olive oil', '3 shallots, thinly sliced', '6 cloves garlic, coarsely chopped', '2 cups arrabbiata pasta sauce', '1/4 cup chicken broth', '3 tablespoons red wine vinegar', '2 pounds boneless, skinless chicken thighs', '1 cup plain yogurt, divided', '3 tablespoons paprika', 'Add all ingredients to list'],
#             'directions': ['microwave', 'eat']}
    
#     return HttpResponse(json.dumps(data), content_type='application/json')
