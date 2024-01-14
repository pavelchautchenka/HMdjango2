from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest

from .forms import RecipeForm, IngredientsForm
from .models import Recipe


def home(request: WSGIRequest):
    return render(request, 'home.html', {"recipes": Recipe.objects.all()})


@login_required
def create_recipe(request: WSGIRequest):

    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Файлы находятся отдельно!
        if form.is_valid():
            recipe: Recipe = form.save(commit=False)  # Не сохранять в базу рецепт, а вернуть его объект.
            recipe.user = request.user
            recipe.save()  # Сохраняем в базу объект.

            form.save_m2m()  # Сохраняем отношения many to many для ингредиентов и рецепта.
            return HttpResponseRedirect("/")

    return render(request, 'recipe-form.html', {'form': form})


def register(request: WSGIRequest):
    pass

@login_required
def create_ingredients(request: WSGIRequest):

    form = IngredientsForm()

    if request.method == 'POST':
        form = IngredientsForm(request.POST, request.FILES)  # Файлы находятся отдельно!
        if form.is_valid():
            ingredient = form.save(commit=False)
            # Не сохранять в базу рецепт, а вернуть его объект.
            ingredient.save()  # Сохраняем в базу объект.
            form.save_m2m()  # Сохраняем отношения many to many для ингредиентов и рецепта.
            return HttpResponseRedirect(reverse("create-recipe"))

    return render(request, 'ingredient-form.html', {'form': form})


def register(request: WSGIRequest):
    pass