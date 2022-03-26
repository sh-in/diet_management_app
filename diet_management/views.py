from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from .models import Meal
from . import mixins
from . import forms

# Create your views here.
class MealList(ListView):
    model = Meal
    context_object_name = "meals"

class MealCreate(CreateView):
    # define initial variable
    def __init__(self):
        self.params = {
            "Message": "Please fill the blank.",
            "form": forms.MealPost(),
        }

    # GET process
    def get(self, request):
        return render(request, "diet_management/meal_form.html", context=self.params)

    # POST process
    def post(self, request):
        if request.method == "POST":
            self.params["form"] = forms.MealPost(request.POST)

            # if form is valid
            if self.params["form"].is_valid():
                # save information to the database
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
        print(calendar_context)
        context.update(calendar_context)
        return context

class MealDetail(DetailView):
    model = Meal
    context_object_name = "meal"

class MealUpdate(UpdateView):
    model = Meal
    fields = ("title", "calory", "protein", "carb", "fat", "date")
    success_url = reverse_lazy("week_with_meal")

class MealDelete(DeleteView):
    model = Meal
    context_object_name = "meal"
    success_url = reverse_lazy("week_with_meal")