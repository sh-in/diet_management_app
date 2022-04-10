from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse

from .models import Meal
from . import mixins
from . import forms

# Create your views here.
# Calendar
class WeekCalendar(mixins.WeekCalendarMixin, mixins.BaseCalendarMixin, TemplateView, LoginRequiredMixin):
    template_name = "diet_management/week.html"
    # set the start day as Sunday
    first_weekday = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context

class WeekWithMealCalendar(LoginRequiredMixin, mixins.WeekWithMealMixin, TemplateView):
    template_name = "diet_management/week_with_meal.html"
    model = Meal
    date_field = 'date'
    # set the start day as Sunday
    first_weekday = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        print(calendar_context)
        print(self.request.user)
        context.update(calendar_context)
        return context

# Meal
class MealCreate(CreateView, LoginRequiredMixin):
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
                # self.params["form"].save(commit=True)
                meal = self.params["form"].save(commit=False)
                meal.user = request.user
                meal.save()
                self.params["Message"] = "Your meal has been sent."
        
        return render(request, "diet_management/meal_form.html", context=self.params)

class MealDetail(DetailView, LoginRequiredMixin):
    model = Meal
    context_object_name = "meal"

class MealUpdate(UpdateView, LoginRequiredMixin):
    model = Meal
    fields = ("title", "calory", "protein", "carb", "fat", "date")
    success_url = reverse_lazy("week_with_meal")

class MealDelete(DeleteView, LoginRequiredMixin):
    model = Meal
    context_object_name = "meal"
    success_url = reverse_lazy("week_with_meal")

# Register, Login, and Logout
#Login
def Login(request):
    #POST
    if request.method == 'POST':
        # get user id and password through form
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        #django authentication
        user = authenticate(username=ID, password=Pass)

        #user authentication
        if user:
            #judge user activation
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("This account is not valid.")
        else:
            return HttpResponse("Wrong Login ID or Password.")
    else:
        return render(request, "diet_management/login.html")

#Logout
@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))

#Home
@login_required
def home(request):
    params = {'UserID': request.user,}
    return render(request, "diet_management/home.html", context=params)

#Registration
class AccountRegistration(TemplateView):
    def __init__(self):
        self.params = {
            "AccountCreate": False,
            "account_form": forms.AccountForm(),
            "add_account_form": forms.AddAcountForm(),
        }
    
    def get(self, request):
        self.params["account_form"] = forms.AccountForm()
        self.params["add_account_form"] = forms.AddAcountForm()
        self.params["AccountCreate"] = False
        return render(request, "diet_management/register.html", context=self.params)

    def post(self, request):
        self.params["account_form"] = forms.AccountForm(data=request.POST)
        self.params["add_account_form"] = forms.AddAcountForm(data=request.POST)

        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # save account data into database
            account = self.params["account_form"].save()
            # hash password
            account.set_password(account.password)
            # save hashed password
            account.save()
            
            add_account = self.params["add_account_form"].save(commit=False)
            # define AcountForm and AddAccountForm one to one
            add_account.user = account
            add_account.save()

            self.params["AccountCreate"] = True
        else:
            print(self.params["account_form"].errors)

        return render(request, "diet_management/register.html", context=self.params)

# PFC
class PFC(TemplateView, LoginRequiredMixin):
    template_name = "diet_management/calc_pfc.html"
    def __init__(self):
        self.params = {
            "pfc_form": forms.PFCBalance(),
        }
    
    def get(self, request):
        self.params["pfc_form"] = forms.PFCBalance()
        return render(request, "diet_management/calc_pfc.html", context=self.params)

    def post(self, request):
        if request.method == "POST":
            self.params["pfc_form"] = forms.PFCBalance(request.POST)

            if self.params["pfc_form"].is_valid():
                pfc = self.params["pfc_form"].save()
                pfc.save()
        
        return render(request, "diet_management/calc_pfc.html", context=self.params)
