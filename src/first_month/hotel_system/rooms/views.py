from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Hotel

def home(request):
    rooms = Room.objects.all()
    hotel = get_object_or_404(Hotel)


    return render(request, 'rooms/home.html', {'room': rooms, 'hotels':hotel})
def reserve(request,pk):
    specific_room = get_object_or_404(Room,pk=pk)
    rooms = Room.objects.all()
    hotel = get_object_or_404(Hotel)
    if specific_room.room_count == 0:
        specific_room.save()
    else:
        specific_room.room_count -= 1
        specific_room.save()
    return render(request, 'rooms/reserve.html', {'room': rooms, 'hotels':hotel})

def checkout(request,pk):
    specific_room = get_object_or_404(Room, pk=pk)
    rooms = Room.objects.all()
    hotel = get_object_or_404(Hotel)
    if specific_room.room_count == 20:
        specific_room.save()
    else:
        specific_room.room_count += 1
        specific_room.save()

    return render(request, 'rooms/checkout.html', {'room': rooms, 'hotels':hotel})

def rate(request,pk):
    rooms = Room.objects.all()
    hotel = get_object_or_404(Hotel)
    hotel.rater_count += 1
    hotel.rated_overall += pk
    hotel.rating = round((hotel.rated_overall / hotel.rater_count),2)
    hotel.save()
    return render(request, 'rooms/rate.html', {'room': rooms, 'hotels':hotel})
