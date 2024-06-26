from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .models import User, Room, Reservation, Invoice
from .serializers import UserSerializer, RoomSerializer, ReservationSerializer, InvoiceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    

def index(request):
    return render(request, 'index.html')

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reservation submitted successfully.')
    else:
        form = ReservationForm()
    
    return render(request, 'reservation.html', {'form': form})

def invoices_view(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices.html', {'invoices': invoices})


def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def kingpost_view(request):
    return render(request, 'kingpost.html')

def residence_view(request):
    return render(request, 'residencies.html')

def tavern_view(request):
    return render(request, 'tavern.html')

def cafe_chumba_view(request):
    return render(request, 'chumba.html')

def conference_view(request):
    return render(request, 'conference.html')

def party_view(request):
    return render(request, 'conference.html')

def folksgym_view(request):
    return render(request, 'gym.html')

def contact_view(request):
    return render(request, 'contact.html')

def booking_view(request):
    return render(request, 'booking.html')
