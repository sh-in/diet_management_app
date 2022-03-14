from unicodedata import name
from django.urls import path
from .views import MealList, WeekCalendar

urlpatterns = [
    path("", MealList.as_view(), name="meal_list"),
    path("week/", WeekCalendar.as_view(), name="week"),
    path("week/<int:year>/<int:month>/<int:day>/", WeekCalendar.as_view(), name="week"),
]