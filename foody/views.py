from django.shortcuts import render
from .models import Meals, Category, Reservation, AboutUs, TeamMembers
from .models import ServiceCards, HeroContainer, Testimonials
from .forms import ReserveTableForm

# Menu List


def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()

    context = {
        'meal_list': meal_list,
        'categories': categories,
    }

    return render(request, 'list.html', context)

# Meal Detail


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)

    context = {'meal_detail': meal_detail, }

    return render(request, 'detail.html', context)

# Home Page


def home(request):
    about = AboutUs.objects.last()
    cards = ServiceCards.objects.all()
    hero = HeroContainer.objects.last()
    testimonials = Testimonials.objects.all()

    context = {
        'about': about,
        'cards': cards,
        'hero': hero,
        'testimonials': testimonials,
    }

    return render(request, 'home.html', context)

# About Page


def about_us(request):
    about = AboutUs.objects.last()
    team = TeamMembers.objects.all()

    context = {
        'about': about,
        'team': team,
    }

    return render(request, 'about.html', context)

# Reservation Form


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}

    return render(request, 'reservation.html', context)
