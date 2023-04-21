from django.urls import path
from . import views


app_name = 'booking'


urlpatterns = [
    path('', views.home, name='home'),
    path('menu.html', views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail'),
]