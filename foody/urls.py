from django.urls import path
from . import views


app_name = 'booking'


urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.meal_list, name='meal_list'),
    path('menu/<slug:slug>', views.meal_detail, name='meal_detail'),
    path('reservation', views.reserve_table, name='reserve_table'),
]