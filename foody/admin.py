from django.contrib import admin
from .models import Meals, Category, Reservation

admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(Reservation)