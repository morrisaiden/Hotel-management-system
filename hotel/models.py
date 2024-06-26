from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('front_desk', 'Front Desk'),
        ('housekeeping', 'Housekeeping')
    ]
    role = models.CharField(max_length=20, choices=ROLES)

    groups = models.ManyToManyField(
        Group,
        related_name='hotel_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='hotel_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='hotel_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='hotel_user',
    )

class Room(models.Model):
    ROOM_STATUS = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance')
    ]
    number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=ROOM_STATUS)
    amenities = models.TextField()

class Reservation(models.Model):
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guest_name} - Room: {self.room}, Check-in: {self.check_in}, Check-out: {self.check_out}"

class Invoice(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
