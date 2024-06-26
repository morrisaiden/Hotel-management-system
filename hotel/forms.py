# hotel/forms.py

from django import forms
from hotel.models import Reservation  # Assuming Reservation model is defined in hotel/models.py

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_name', 'guest_email', 'check_in', 'check_out', 'room']
