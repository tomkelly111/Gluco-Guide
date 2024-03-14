from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    food = models.CharField(max_length=200, unique=True)
    prior_reading = models.DecimalField(max_digits=5, decimal_places=2)
    post_reading = models.DecimalField(max_digits=5, decimal_places=2)
    individual = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_item")
    reading_difference = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, default=0)
    
    def update_reading_difference(self):
        """
        Provide differendec of reading before and after food consumption
        """
        self.reading_difference = (self.post_reading - self.prior_reading)
        self.save()