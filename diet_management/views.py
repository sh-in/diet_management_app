from calendar import firstweekday
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Meal
from . import mixins

# Create your views here.
class MealList(ListView):
    model = Meal
    context_object_name = "meals"

class WeekCalendar(mixins.WeekCalendarMixin, mixins.BaseCalendarMixin, TemplateView):
    template_name = "diet_management/week.html"
    # set the start day as Sunday
    first_weekday = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context