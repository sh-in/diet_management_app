from django.db import models

# model for single meal
class Meal(models.Model):
    title = models.CharField(max_length=50)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carb = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title