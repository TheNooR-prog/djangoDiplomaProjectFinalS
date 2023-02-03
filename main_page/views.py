from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Dish, About, WhyUs, StatsCounter, Testimonials, Event, Chef, Gallery
from .forms import UserReservationForm, UserContactForm


def main_page(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        contact = UserContactForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')
        if contact.is_valid():
            contact.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    reservation = UserReservationForm()
    about = About.objects.first()
    why_us = WhyUs.objects.first()
    stats_counter = StatsCounter.objects.filter(is_visible=True)
    testimonials = Testimonials.objects.filter(is_visible=True)
    events = Event.objects.filter(is_visible=True)
    chefs = Chef.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    contact = UserContactForm()

    data = {'categories': categories,
            'dishes': dishes,
            'reservation_form': reservation,
            'about': about,
            'why_us': why_us,
            'stats_counter': stats_counter,
            'testimonials': testimonials,
            'range': range(1, 6),
            'events': events,
            'chefs': chefs,
            'gallery': gallery,
            'contact_form': contact,
            }

    return render(request, 'main_page.html', context=data)
