import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Store,Recipe,Ingredient,RecipeIngredient,Coupon

#This is the home page
def home(request):
    details = [] # this stores all the data that is needed to be passed to the html page
    recipes = Recipe.objects.all() #This returns all the recipes in the database
    for i in recipes:
        dic = {} # this is the template for details
        dic['recipe_name'] = i.name
        dic['type'] = i.type
        dic['id'] = i.id
        dic['image'] = i.image
        ri = RecipeIngredient.objects.filter(r_id = i.id) # this returns all the connectios between ingredients and given recipe
        a = [] # this stores the list of names of ingredients in the given recipe
        for j in ri:
            a.append(j.i_id.name)
        dic['Ingredient_list'] = a
        details.append(dic)
    # print(details)
    context = {
        'recipes': details,
    }
    return render(request,'stores/home.html',context)


def result(request,result_id):
    recipe = Recipe.objects.filter(id = result_id) #This returns the recipe of id same as result_id
    ri = RecipeIngredient.objects.filter(r_id = result_id) # This returns all the connections between ingredients and given recipe
    details = [] # this stores all the data that is needed to be passed to the html page
    for j in ri:
        dic = {} # this is the template for details
        coupons = Coupon.objects.filter(i_id = j.i_id.id).order_by('price') # This returns all coupons of given ingredient sorted by price(low to high)
        dic['ingredient_name'] = j.i_id.name
        dic['image'] = j.i_id.image
        dic['unit'] = j.i_id.unit
        dic['quantity'] = j.quantity
        if coupons:# if coupons are not blank then store their data in dic
            store = Store.objects.filter(id = coupons[0].s_id.id) # this returns the store of the given coupon
            dic['store_name'] = store[0].name
            dic['address'] = store[0].address
            dic['price'] = coupons[0].price
        else:
            dic['store_name'] = "This product is not available"
            dic['address'] = ""
            dic['price'] = "!!"
        details.append(dic)
    # print(details)

    context = {
        'recipe_name': recipe[0].name,
        'recipe_image': recipe[0].image,
        'recipe_description': recipe[0].description,
        'list_of_ingredients': details,
    }
    return render(request,'stores/result.html', context)
