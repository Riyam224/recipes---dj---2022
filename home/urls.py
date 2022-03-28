from django.urls import path 
from . import views 




urlpatterns = [
    path('' , views.RecipeList.as_view() , name='recipe_list'),
    path('<int:pk>/' , views.RecipeDetail.as_view() , name='recipe'),
    path('category/<str:category>/' , views.property_by_category , name='property_by_category'),
   
    
]
