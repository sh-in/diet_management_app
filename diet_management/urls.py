from django.urls import path
from .views import MealList

urlpatterns = [
    path("", MealList.as_view(), name="meal_list"),
]