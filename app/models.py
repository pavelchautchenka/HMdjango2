from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255,)
    weight = models.CharField(max_length=10, null=True, blank=True)
    calories = models.PositiveIntegerField(verbose_name='calories', default=1, null=True, blank=True)
    description = models.TextField(verbose_name="Ingredient Description", null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание рецепта")
    preview_image = models.ImageField(upload_to='images/', verbose_name="Картинка", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    time_minutes = models.IntegerField(
        validators=[],
        default=1,
        verbose_name="Время приготовления",
        help_text="В минутах"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient,  verbose_name="Ингредиенты")

    class Category(models.TextChoices):
        breakfast = ('B', 'Завтрак')
        dinner = ('D', 'Обед')
        supper = ('S', 'Ужин')

    category = models.CharField(max_length=1, choices=Category.choices, verbose_name="Прием пищи")

    class Meta:
        ordering = ("-created_at",)
