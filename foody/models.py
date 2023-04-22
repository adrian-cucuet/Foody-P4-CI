from django.db import models
from django.utils.text import slugify
from datetime import datetime


# Meal List


class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='img/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.name


# Meal Category


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# Meal Detail


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)

    context = {'meal_detail': meal_detail, }

    return render(request, 'detail.html', context)


# Reservation Form


class Reservation(models.Model):
    people_choices = (
        ('one', '1 Person'),
        ('two', '2 People'),
        ('three', '3 People'),
        ('four', '4 People'),
        ('five_plus', '5+ People'),
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    number_of_people = models.CharField(
        max_length=10, choices=people_choices, default='one')
    Date = models.DateField(default=datetime.today)
    time = models.TimeField(default=datetime.now)

    def __str__(self):
        return self.name


# Dining Times


class DiningTimes(models.Model):
    name = models.CharField(max_length=30)
    breakfast = models.TextField()
    breakfast_weekend = models.TextField(null=True, blank=True)
    lunch = models.TextField()
    lunch_weekend = models.TextField(null=True, blank=True)
    dinner = models.TextField()
    dinner_weekend = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Dining Times'
        verbose_name_plural = 'Dining Times'

    def __str__(self):
        return self.name

# About Us


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    section_title = models.CharField(max_length=30)
    content = models.TextField()
    number_a = models.IntegerField()
    title_a_small = models.CharField(max_length=30)
    title_a_big = models.CharField(max_length=30)
    number_b = models.IntegerField()
    title_b_small = models.CharField(max_length=30)
    title_b_big = models.CharField(max_length=30)
    image_left_up = models.ImageField(upload_to='img/aboutus/')
    image_left_down = models.ImageField(upload_to='img/aboutus/')
    image_right_up = models.ImageField(upload_to='img/aboutus/')
    image_right_down = models.ImageField(upload_to='img/aboutus/')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


class TeamMembers(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='img/team/')
    facebook = models.TextField()
    twitter = models.TextField()
    instagram = models.TextField()

    class Meta:
        verbose_name = 'Team Members'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name


# Service Cards


class ServiceCards(models.Model):
    title = models.CharField(max_length=50)
    icon = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Service Cards'
        verbose_name_plural = 'Service Cards'

    def __str__(self):
        return self.title


# Hero


class HeroContainer(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='img/hero/')
    cta_text = models.TextField()

    class Meta:
        verbose_name = 'Hero Container'
        verbose_name_plural = 'Hero Container'

    def __str__(self):
        return self.name


# Testimonials


class Testimonials(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='img/testimonials/')

    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name
