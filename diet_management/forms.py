from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Meal, Account
from django.contrib.auth.models import User

class MealPost(forms.ModelForm):
    class Meta():
        model = Meal
        fields = ("title", "calory", "protein", "fat", "carb", "date")
        labels = {
            'title': 'Meal name',
            'calory': 'Calory',
            'protein': 'Protein(g)',
            'fat': 'Fat(g)',
            'carb': 'Carbs(g)',
            'date': 'Date',
        }

        widgets = {
            "date": forms.SelectDateWidget
        }

        help_texts = {
            'calory': 'kcal',
            'protein': 'g',
            'fat': 'g',
            'carb': 'g',
        }

# define user authenticate field
class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="password")

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': "User ID",
            'email': "Mail"
        }

# define fields which is not defined by django user authenticate
class AddAcountForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = ('last_name', 'first_name')
        labels = {
            'last_name': "Last Name",
            'first_name': "First Name",
        }

# PFC
# This doesn't work
class PFCBalance(forms.ModelForm):
    class Meta():
        model = Account
        fields = (
            'calory',
            'protein',
            'fat',
            'carb',
        )
        labels = {
            'calory': "Calory",
            'protein': "Protein",
            'fat': "Fat",
            'carb': "Carb",
        }