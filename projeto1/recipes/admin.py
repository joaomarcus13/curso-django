from django.contrib import admin

from recipes.models import Category, Recipe

# 95751535
# Register your models here.


# registrar models para aparecer o crud na area administrativa do django
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

# ou


admin.site.register(Category, CategoryAdmin)
