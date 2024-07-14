from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class CoffeeTypes(models.Model):
    COFFEE_TYPES_CHOICE = [
        ("BLK", "BLACK"),
        ("CUP", "CUPPUCCINO"),
        ("MOC", "MOCHA"),
        ("CBN", "COFFEE_BEANS"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="coffee_img/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=COFFEE_TYPES_CHOICE, default="BLK")
    description = models.TextField(default="", blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# One to many relation - user & review
class CoffeeReview(models.Model):
    coffee = models.ForeignKey(
        CoffeeTypes, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.coffee.name}"


# Many to many relation - stores & coffees
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    coffee_varieties = models.ManyToManyField(CoffeeTypes, related_name="stores")

    def __str__(self):
        return self.name


# One to one relation - coffee & certificates
class CoffeeCerts(models.Model):
    coffee = models.OneToOneField(
        CoffeeTypes, on_delete=models.CASCADE, related_name="certificates"
    )
    cert_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.coffee.name}"
