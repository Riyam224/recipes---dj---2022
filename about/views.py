
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from home.models import Recipe
from  django.conf import settings


def about(request):
    recipes = Recipe.objects.all()
    return render(request , 'about/about.html' , 
    {
        'recipes': recipes
    })


def contact(request):
    recipes = Recipe.objects.all()

    if request.method == 'POST':
        name  = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail(
            name,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )

    return render(request , 'about/contact.html', {
        'recipes': recipes
    })