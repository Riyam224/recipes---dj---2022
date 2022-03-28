
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(_("name"), max_length=250)
    image = models.ImageField(_("image"), upload_to='recipe/')
    desc = models.TextField(_("description"))
    prep_time = models.IntegerField(_("prep time "))
    cook_time = models.IntegerField(_("cook time"))
    serving_num = models.IntegerField(_("serving number"))
    category = models.ForeignKey("Category", related_name='recipe_category', verbose_name=_("category"), on_delete=models.CASCADE)
    tags = TaggableManager()


    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(_("name"), max_length=250)



    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name
