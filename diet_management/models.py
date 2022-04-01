from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import model_to_dict

# model for single meal
class Meal(models.Model):
    title = models.CharField(max_length=50)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carb = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username