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