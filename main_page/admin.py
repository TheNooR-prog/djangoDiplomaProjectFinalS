from django.contrib import admin
from .models import Category, Dish, UserReservation, About, WhyUs, StatsCounter, Testimonials, Event, Chef, Gallery, UserContact

# Register your models here.
admin.site.register(Category)
admin.site.register(UserReservation)
admin.site.register(About)
admin.site.register(WhyUs)
admin.site.register(StatsCounter)
admin.site.register(Testimonials)
admin.site.register(Event)
admin.site.register(Chef)
admin.site.register(Gallery)
admin.site.register(UserContact)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name', ), }


