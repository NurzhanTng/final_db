from django.urls import path
from .views import (
    CountryListAPIView,
    VoyageListAPIView,
    CityListAPIView,
    SightseeingListAPIView,
    AirlineListAPIView,
    TicketListAPIView,
    FlightListAPIView,
    AirportListAPIView,
    ClientByEmailAndPasswordAPIView,
    PaymentRetrieveAPIView,
    AirplaneRetrieveAPIView,
    TicketPaymentsByTicketAPIView,
    TicketCreateAPIView,
    ClientCreateAPIView,
    PaymentCreateAPIView,
    TicketPaymentCreateAPIView
)

urlpatterns = [
    path('clients/', ClientByEmailAndPasswordAPIView.as_view(), name='client-by-email-password'),
    path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment-detail'),
    path('airplanes/<int:pk>/', AirplaneRetrieveAPIView.as_view(), name='airplane-detail'),
    path('ticket_payments/<int:ticket_id>/', TicketPaymentsByTicketAPIView.as_view(), name='ticket-payment-list'),
    
    path('tickets/', TicketCreateAPIView.as_view(), name='ticket-create'),
    path('clients/', ClientCreateAPIView.as_view(), name='client-create'),
    path('payments/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('ticket_payments/', TicketPaymentCreateAPIView.as_view(), name='ticket-payment-create'),

    path('countries/', CountryListAPIView.as_view(), name='country-list'),
    path('voyages/', VoyageListAPIView.as_view(), name='voyage-list'),
    path('cities/', CityListAPIView.as_view(), name='city-list'),
    path('sightseeings/', SightseeingListAPIView.as_view(), name='sightseeing-list'),
    path('airlines/', AirlineListAPIView.as_view(), name='airline-list'),
    path('tickets/', TicketListAPIView.as_view(), name='ticket-list'),
    path('flights/', FlightListAPIView.as_view(), name='flight-list'),
    path('airports/', AirportListAPIView.as_view(), name='airport-list'),
]
