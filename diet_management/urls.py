from unicodedata import name
from django.urls import path
from .views import MealList, WeekCalendar, WeekWithMealCalendar

urlpatterns = [
    path("", MealList.as_view(), name="meal_list"),
    path("week_with_meal/", WeekWithMealCalendar.as_view(), name="week_with_meal"),
    path("week_with_meal/<int:year>/<int:month>/<int:day>/", WeekWithMealCalendar.as_view(), name="week_with_meal"),
]