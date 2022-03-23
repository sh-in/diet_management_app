from django import forms
from .models import Meal

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