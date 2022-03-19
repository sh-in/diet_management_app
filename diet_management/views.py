from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from .models import Meal
from . import mixins
from . import forms

# Create your views here.
class MealList(ListView):
    model = Meal
    context_object_name = "meals"

class MealCreate(CreateView):
    def __init__(self):
        self.params = {
            "Message": "Please fill the blank.",
            "form": forms.MealPost(),
        }

    def get(self, request):
        return render(request, "diet_management/meal_form.html", context=self.params)

    def post(self, request):
        if request.method == "POST":
            self.params["form"] = forms.MealPost(request.POST)

            if self.params["form"].is_valid():
                self.params["form"].save(commit=True)
                self.params["Message"] = "Your meal has been sent."
        
        return render(request, "diet_management/meal_form.html", context=self.params)

class WeekCalendar(mixins.WeekCalendarMixin, mixins.BaseCalendarMixin, TemplateView):
    template_name = "diet_management/week.html"
    # set the start day as Sunday
    first_weekday = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context

class WeekWithMealCalendar(mixins.WeekWithMealMixin, TemplateView):
    template_name = "diet_management/week_with_meal.html"
    model = Meal
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context