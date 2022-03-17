from calendar import firstweekday
from dataclasses import field
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from .models import Meal
from . import mixins

# Create your views here.
class MealList(ListView):
    model = Meal
    context_object_name = "meals"

class MealCreate(CreateView):
    model = Meal
    fields = "__all__"
    success_url = reverse_lazy("week_with_meal")

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