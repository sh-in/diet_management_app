from django.urls import path
from .views import MealCreate, MealDelete, MealUpdate, WeekWithMealCalendar, MealDetail, AccountRegistration, Login, Logout, home

urlpatterns = [
    path("", Login, name="Login"),
    path("logout", Logout, name="Logout"),
    path("register", AccountRegistration.as_view(), name="register"),
    path("home", home, name="home"),
    path("week_with_meal/", WeekWithMealCalendar.as_view(), name="week_with_meal"),
    path("week_with_meal/<int:year>/<int:month>/<int:day>/", WeekWithMealCalendar.as_view(), name="week_with_meal"),
    path("create/", MealCreate.as_view(), name="create"),
    path("detail/<int:pk>", MealDetail.as_view(), name="detail"),
    path("update/<int:pk>", MealUpdate.as_view(), name="update"),
    path("delete/<int:pk>", MealDelete.as_view(), name="delete"),
]