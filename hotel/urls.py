from django.urls import path, include
from hotel import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoomViewSet, ReservationViewSet, InvoiceViewSet, reservation_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import index

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('invoices/', views.invoices_view, name='invoices'),
    path('users/', views.users_view, name='users'),
    path('kingpost/', views.kingpost_view, name='kingpost'),
    path('residence/', views.residence_view, name='residence'),
    path('tavern/', views.tavern_view, name='tavern'),
    path('cafe_chumba/', views.cafe_chumba_view, name='cafe_chumba'),
    path('conferences/', views.conference_view, name='conferences'),
    path('parties', views.party_view, name='parties'),
    path('folksgym/', views.folksgym_view, name='folksgym'),
    path('contact-us/', views.contact_view, name='contact'),
    path('book/', views.booking_view, name='booking'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reserve/', reservation_view, name='reservation'),
]