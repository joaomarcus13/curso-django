from django.urls import path

from . import views

app_name = 'recipes'  # => namespace  recipes:recipe, recipes:home


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
