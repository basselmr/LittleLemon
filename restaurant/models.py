from django.db import models
from django.db.models import Model

# Create your models here.
class Booking(Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField()
    def get_item(self):
        return f'{self.Title} : {str(self.price)}'
    def __str__(self) -> str:
        return f'{self.Title} : {str(self.price)}'



