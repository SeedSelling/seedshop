from django.db import models

class Seed(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
 

    farmer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.farmer_name} - {self.seed.name}"

class SeedVariety(models.Model):
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, related_name='varieties')
    name = models.CharField(max_length=100)      # e.g. Wheat – Lokwan, Sharbati
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.seed.name} - {self.name}"
        
        # Create your models here.
