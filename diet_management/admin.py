from django.contrib import admin
from diet_management.models import Account, Meal

# Register your models here.
admin.site.register(Meal)
admin.site.register(Account)