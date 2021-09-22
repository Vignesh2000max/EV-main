from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import bookedSlotLogDetail
from datetime import date

def home(request):
    history = bookedSlotLogDetail.objects.filter(station=request.user)
    if request.method == 'GET':
        return render(request, 'manager/home.html', {'histories':history})
    else:
        filter_option = request.POST['filter_charge_history']
        if filter_option == 'all':
            return render(request, 'manager/home.html', {'histories':history})
        elif filter_option == 'date':
            today = date.today()
            history = bookedSlotLogDetail.objects.filter(station=request.user, booked_date=today)
            return render(request, 'manager/home.html', {'histories':history})
        else:
            return render(request, 'manager/home.html', {'histories':history, 'error':'Wrong filter option'})

def manage_slots(request):
    today = date.today()
    history = bookedSlotLogDetail.objects.filter(station=request.user, booked_date=today)
    if request.method == 'GET':
        return render(request, 'manager/manage_slots.html', {'histories': history})

@login_required
def delete_slot(request):
    print("INSIDE")
    slot = get_object_or_404(bookedSlotLogDetail, id = request.POST['slot_id'])
    if request.method =='POST':
        if slot:
            slot.delete()
            return redirect('manager:manage_slots')
        else:
            return redirect('manager:manage_slots')