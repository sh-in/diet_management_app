from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView

from .models import Meal

# Create your views here.
class MealList(ListView):
    model = Meal
    context_object_name = "meals"