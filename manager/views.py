from django.shortcuts import render, redirect, HttpResponse
from main_page.models import UserReservation, UserContact
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservations_list(request):
    reservations = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'reservations': reservations,
    })

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contacts_list(request):
    contacts = UserContact.objects.filter(is_processed=False)
    return render(request, 'contacts_list.html', context={
        'contacts': contacts,
    })

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_contact(request, pk):
    UserContact.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contacts_list')