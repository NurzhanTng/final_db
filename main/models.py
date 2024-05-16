from django.db import models


class Clients(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=500)


class Benefits(models.Model):
    benefit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=2)


class Airports(models.Model):
    airport_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)


class Airlines(models.Model):
    airline_id = models.AutoField(primary_key=True)
    image_url = models.URLField(max_length=500)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Voyages(models.Model):
    voyage_id = models.AutoField(primary_key=True)
    departure_airport = models.ForeignKey(Airports, related_name='departure_airport', on_delete=models.CASCADE)
    destination_airport = models.ForeignKey(Airports, related_name='destination_airport', on_delete=models.CASCADE)


class Airplanes(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    airline = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    onboard_number = models.CharField(max_length=255)
    capacity = models.IntegerField()


class Flights(models.Model):
    flight_id = models.AutoField(primary_key=True)
    voyage = models.ForeignKey(Voyages, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplanes, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    voyage = models.ForeignKey(Voyages, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplanes, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    passport_id = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    citizenship = models.CharField(max_length=255)


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateField()
    payment_operator = models.CharField(max_length=255)
    cart_id = models.CharField(max_length=255)


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)


class TicketPayments(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE, primary_key=True)


class BoughtServices(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, primary_key=True)


class Seats(models.Model):
    seat_id = models.AutoField(primary_key=True)
    airplane = models.ForeignKey(Airplanes, on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=50)
    seat_index_x = models.IntegerField()
    seat_index_y = models.IntegerField()


class Sightseeings(models.Model):
    sightseeing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
