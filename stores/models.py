from contextlib import nullcontext
from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.
# This table contains deatils about all nearby stores
class Store(models.Model):
    id = models.AutoField(primary_key = True)
    address = models.CharField(max_length = 500, null=True)
    name = models.CharField(max_length= 200)
    class Meta:
        db_table = 'Store'
    def __str__(self):
        return self.name


#This table contains details about all the recipes
class Recipe(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 200)
    type = models.CharField(max_length = 200,null=True)
    description = models.CharField(max_length = 250, null=True)
    image = models.ImageField(upload_to = 'recipe-images/')
    class Meta:
        db_table = 'Recipe'
    def __str__(self):
        return self.name

#This table contains details about all the Ingredients
class Ingredient(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 200)
    unit = models.CharField(max_length= 10, help_text = 'Enter SI Unit only like kg or ltr or piece', null = True)
    image = models.ImageField(upload_to = 'ingredient-images/', null = True)
    class Meta:
        db_table = 'Ingredient'
    def __str__(self):
        return self.name


#This table contains the connections between recipe and ingredients along with quantity required.
class RecipeIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    quantity =  models.IntegerField(help_text = 'Enter SI Unit only like kg or ltr or piece')
    r_id = models.ForeignKey(Recipe,on_delete=models.CASCADE, null=True)
    i_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)


#This table contains the connections between stores and ingredients along with price.
class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    s_id = models.ForeignKey(Store,on_delete=models.CASCADE, null=True)
    i_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    price  =  models.IntegerField()
