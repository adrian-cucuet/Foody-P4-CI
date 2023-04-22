from django.contrib import admin
from .models import Meals, Category, Reservation, AboutUs, TeamMembers
from .models import ServiceCards, HeroContainer, Testimonials
from django_summernote.admin import SummernoteModelAdmin


class AboutUsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


class ServiceCardsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


class HeroContainerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'title')


admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(Reservation)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(TeamMembers)
admin.site.register(ServiceCards, ServiceCardsAdmin)
admin.site.register(HeroContainer, HeroContainerAdmin)
admin.site.register(Testimonials)