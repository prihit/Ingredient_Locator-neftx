from django.contrib import admin

from .models import Store,Recipe,Ingredient,RecipeIngredient,Coupon
# Register your models here.

admin.site.register(Store)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Coupon)