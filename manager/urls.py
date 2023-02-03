from django.urls import path
from .views import reservations_list, update_reservation, contacts_list, update_contact

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve'),
    path('contacts/', contacts_list, name='contacts_list'),
    path('contacts/update/<int:pk>/', update_contact, name='update_contact'),
]

