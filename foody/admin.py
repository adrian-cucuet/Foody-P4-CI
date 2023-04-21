from django.contrib import admin
from .models import Meals, Category, Reservation, AboutUs, TeamMembers
from django_summernote.admin import SummernoteModelAdmin


class AboutUsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(Reservation)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(TeamMembers)