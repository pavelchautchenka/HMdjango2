from django.urls import path

from .views import create_recipe, home, create_ingredients

# /recipe/

urlpatterns = [
    path('create-ingredients/', create_ingredients, name='create-ingredients'),
    path('create-recipe/', create_recipe, name='create-recipe')
]
