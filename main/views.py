from django.shortcuts import render
from rest_framework import generics
from rest_framework.status import *
from rest_framework.response import Response
from .models import (Clients, Countries, Voyages, Cities, Sightseeings, Airlines, Airplanes, Tickets, Flights,
                     Airports, Payments, TicketPayments)
from .serializers import (CountrySerializer, VoyageSerializer, CitySerializer, SightseeingSerializer,
                          AirlineSerializer, ClientSerializer, PaymentSerializer, AirplaneSerializer,
                          TicketSerializer, FlightSerializer, AirportSerializer, TicketPaymentSerializer)


class CountryListAPIView(generics.ListAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer


class VoyageListAPIView(generics.ListAPIView):
    queryset = Voyages.objects.all()
    serializer_class = VoyageSerializer


class CityListAPIView(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer


class SightseeingListAPIView(generics.ListAPIView):
    queryset = Sightseeings.objects.all()
    serializer_class = SightseeingSerializer


class AirlineListAPIView(generics.ListAPIView):
    queryset = Airlines.objects.all()
    serializer_class = AirlineSerializer


class TicketListAPIView(generics.ListAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer


class FlightListAPIView(generics.ListAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightSerializer


class AirportListAPIView(generics.ListAPIView):
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer


class ClientByEmailAndPasswordAPIView(generics.RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    def get_object(self):
        queryset = self.get_queryset()
        email = self.request.query_params.get('email')
        password = self.request.query_params.get('password')

        # Retrieve the client with the provided email and password
        try:
            client = queryset.get(email=email, password=password)
            return client
        except Clients.DoesNotExist:
            raise HTTP_404_NOT_FOUND


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    def get_object(self):
        queryset = self.get_queryset()
        payment_id = self.kwargs.get('pk')  # Assuming the URL pattern includes the payment ID

        # Retrieve the payment with the provided ID
        try:
            payment = queryset.get(pk=payment_id)
            return payment
        except Payments.DoesNotExist:
            raise HTTP_404_NOT_FOUND


class AirplaneRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Airplanes.objects.all()
    serializer_class = AirplaneSerializer

    def get_object(self):
        queryset = self.get_queryset()
        airplane_id = self.kwargs.get('pk')  # Assuming the URL pattern includes the airplane ID

        # Retrieve the airplane with the provided ID
        try:
            airplane = queryset.get(pk=airplane_id)
            return airplane
        except Airplanes.DoesNotExist:
            raise HTTP_404_NOT_FOUND


class TicketPaymentsByTicketAPIView(generics.ListAPIView):
    serializer_class = TicketPaymentSerializer

    def get_queryset(self):
        ticket_id = self.kwargs.get('ticket_id')  # Assuming the URL pattern includes the ticket ID
        try:
            queryset = TicketPayments.objects.filter(ticket_id=ticket_id)
            return queryset
        except TicketPayments.DoesNotExist:
            raise HTTP_404_NOT_FOUND


class TicketCreateAPIView(generics.CreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)


class TicketPaymentCreateAPIView(generics.CreateAPIView):
    queryset = TicketPayments.objects.all()
    serializer_class = TicketPaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
