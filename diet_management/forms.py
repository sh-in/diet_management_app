from dataclasses import fields
from django import forms
from .models import Meal

class MealPost(forms.ModelForm):
    class Meta():
        model = Meal
        fields = "__all__"
        widgets = {
            "date": forms.SelectDateWidget
        }
        lables = {
            "title": "Meal name",
            "calory": "Calory",
            "protein": "Protein(g)",
            "fat": "Fat(g)",
            "carb": "Carbs(g)",
            "date": "Date",
        }
