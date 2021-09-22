from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from chargeStationManager.models import ChargePoint
from .models import bookedSlotLogDetail
from datetime import date

def chargeSlotsCaculation(cp, slots):
    time_slots = []
    slot_s = {}
    slice_start = 0
    for p in cp:
        for i in range(6, 18):
            for j in range(1, 4):
                if j == 1:
                    if i < 10:
                        time = "0"+str(i)+":00:00"
                    else:
                        time = str(i)+":00:00"
                elif j == 2:
                    if i < 10:
                        time = "0"+str(i)+":20:00"
                    else:
                        time = str(i)+":20:00"
                else:
                    if i < 10:
                        time = "0"+str(i)+":40:00"
                    else:
                        time = str(i)+":40:00"
                if slots:
                    t = {"time":time,
                        "status":"not booked",
                        "point":p.point_number }
                    for slot in slots:
                        if slot.charge_point_number == p.point_number:
                            if time == str(slot.slot_booked_time):
                                t['status'] = "booked"
                                t['point'] = slot.charge_point_number
                                break
                            else:
                                continue
                    time_slots.append(t)
                else:
                    time_slots.append({
                            "time":time,
                            "status":"not booked",
                            "point":None
                        })
    for i in range(0,len(cp)):
        a = time_slots[slice_start:slice_start+36]
        slot_s[cp[i].point_number]=a
        slice_start+=36

    return slot_s


@login_required
def deleteslot(request):
    slot = get_object_or_404(bookedSlotLogDetail, user = request.user, id = request.POST['slot_id'])
    if request.method =='POST':
        if slot:
            print('found')
            slot.delete()
            return redirect('users:charge')
        else:
            return redirect('users:charge')

def landingHome(request):
    try:  
        if request.user.name:
            if request.user.is_manager == True:
                return redirect('manager:managerHome')
        else:
            return redirect('users:usershome')
    except AttributeError:
        return render(request, 'users/index.html')

@login_required
def charge(request):
    stations = get_user_model().objects.filter(is_manager=True)
    if request.method == 'GET':
        return render(request, 'users/nearby_stations.html', {'stations':stations})
    else:
        if request.POST['search_city'] == 'all':
            return render(request, 'users/nearby_stations.html', {'stations':stations})
        else:
            search_station = get_user_model().objects.filter(is_manager=True, city=request.POST['search_city'], area=request.POST['area'])
            return render(request, 'users/nearby_stations.html', {'stations':search_station})

@login_required
def bookSlot(request, st_name):
    today = date.today()
    station = get_object_or_404(get_user_model(), station_name=st_name)
    cp = ChargePoint.objects.filter(station_id=station)
    slots = bookedSlotLogDetail.objects.filter(station=station, booked_date=today).order_by('charge_point_number','slot_booked_time')
    
    slot_s = chargeSlotsCaculation(cp, slots)

    if request.method == 'GET':
        return render(request, 'users/book_slots.html',{'station':station, 'cp':cp, 'slots':slots, 'slot_s':slot_s})
    else:
        slot_exists = bookedSlotLogDetail.objects.filter(charge_point_number=request.POST['charge_point'],
                                                        slot_booked_time=request.POST['booking_time'],
                                                        booked_date=today)
        if slot_exists:
            return render(request, 'users/book_slots.html',{'station':station, 'cp':cp, 'slots':slots, 'slot_s':slot_s, 'error': 'Slot already taken'})
        else:
            try:
                if request.POST['charge_point'] and request.POST['booking_time']:
                    book_slot=bookedSlotLogDetail(user=request.user,
                                                station=station,
                                                charge_point_number=request.POST['charge_point'],
                                                slot_booked_time=request.POST['booking_time'])
                    book_slot.save()
                return redirect('users:charge')
            except ValueError:
                return render(request, 'users/book_slots.html',{'station':station, 'cp':cp, 'slots':slots, 'slot_s':slot_s, 'error': 'Bad Credentials'})
    
def signup(request, action, u_type=None):
    if request.method == 'GET':
        if(action == 'signup'):
            return render(request, 'users/signup.html', {'usertype':u_type, 'form_opened':True})
        else:
            return render(request, 'users/signup.html', {'form_opened':False})
    else:
        if(request.POST['req_type'] == 'signup'):
            try:
                if(u_type == 'manager'):
                    user = get_user_model().objects.create_user(email = request.POST['email'],
                                                                password = request.POST['password'],
                                                                username = request.POST['uname'],
                                                                contact = request.POST['contact'],
                                                                address = request.POST['address'],
                                                                city = request.POST['city'],
                                                                state = request.POST['state'],
                                                                pin = request.POST['pin'],
                                                                is_manager = True,
                                                                area=request.POST['area'],
                                                                station_name=request.POST['station_name'])
                    login(request, user)
                    for i in range(1,int(request.POST['num_points'])+1):
                        p_num='point '+str(i)
                        charge_point = ChargePoint(station_id=request.user,  point_number=p_num)
                        charge_point.save()
                    return redirect('manager:managerHome')
                else:
                    user = get_user_model().objects.create_user(email = request.POST['email'],
                                                                password = request.POST['password'],
                                                                username = request.POST['uname'],
                                                                contact = request.POST['contact'],
                                                                address = request.POST['address'],
                                                                city = request.POST['city'],
                                                                state = request.POST['state'],
                                                                pin = request.POST['pin'],
                                                                firstname = request.POST['fname'],
                                                                lastname = request.POST['lname'])
                    login(request, user)
                    return redirect('users:usershome')                             
            except IntegrityError:
                return render(request, 'users/signup.html', {'error':'Email already exists', 'usertype':u_type, 'form_opened':True})
            except ValueError:
                return render(request, 'users/signup.html', {'error':'Invalid contact', 'usertype':u_type, 'form_opened':True})
        elif(request.POST['req_type'] == 'signin'):
            user = authenticate(request,email = request.POST['email'], password = request.POST['password'])
            if user is None:
                return render(request, 'users/signup.html', {'loginerror':'Email or Password Incorrect', 'form_opened':False})
            else:
                login(request, user)
                if(user.is_manager == True):
                    return redirect('manager:managerHome')
                else:
                    return redirect('users:usershome')

def logoutUser(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('landingPage')

@login_required
def home(request):
    return render(request, 'users/index.html')

