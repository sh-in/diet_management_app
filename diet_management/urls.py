from unicodedata import name
from django.urls import path
from .views import MealCreate, MealDelete, MealList, MealUpdate, WeekWithMealCalendar, MealDetail

urlpatterns = [
    path("", MealList.as_view(), name="meal_list"),
    path("week_with_meal/", WeekWithMealCalendar.as_view(), name="week_with_meal"),
    path("week_with_meal/<int:year>/<int:month>/<int:day>/", WeekWithMealCalendar.as_view(), name="week_with_meal"),
    path("create/", MealCreate.as_view(), name="create"),
    path("detail/<int:pk>", MealDetail.as_view(), name="detail"),
    path("update/<int:pk>", MealUpdate.as_view(), name="update"),
    path("delete/<int:pk>", MealDelete.as_view(), name="delete"),
]