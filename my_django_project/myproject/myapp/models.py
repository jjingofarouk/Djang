from django.db import models

class Product(models.Model):
    # Define the fields based on your database schema
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    reviews = models.IntegerField()
    category = models.CharField(max_length=50)

    # Optionally, you can add a string representation method
    def __str__(self):
        return self.name
