from django.db import models
from django.utils.text import slugify

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