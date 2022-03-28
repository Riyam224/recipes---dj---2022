
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Recipe , Category
from django.db.models import Count
from taggit.models import Tag


class RecipeList(ListView):
    model = Recipe
    template_name = 'home/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('recipe_category'))
        return context
    

class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'home/recipe.html'




def property_by_category(request,category):
    categories = Category.objects.all()
    my_category = Category.objects.get(name=category)
    recipe_category = Recipe.objects.filter(category=my_category)
    return render(request , 'home/recipe_by_category.html' , 
    {'recipe_category':recipe_category, 'my_category':my_category , 'categories':categories })
    