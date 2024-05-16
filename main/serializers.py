from rest_framework import serializers
from .models import (Clients, Airports, Countries, Voyages, Cities, Sightseeings, Airlines, Tickets, Flights,
                     Airports, Payments, Airplanes, TicketPayments)


class TicketPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPayments
        fields = ['ticket', 'payment']


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplanes
        fields = ['airplane_id', 'airline', 'model', 'onboard_number', 'capacity']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['user_id', 'name', 'surname', 'phone', 'email', 'password', 'date_of_birth']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['payment_id', 'amount', 'currency', 'date', 'payment_operator', 'cart_id']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['country_id', 'name']


class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyages
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class SightseeingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sightseeings
        fields = '__all__'


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = '__all__'
