from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

ROOM_CHOICES = (
	("single", "single"),
	("double","double"),
	("luxe","luxe"),
	("president luxe","president luxe")
	)


class Hotel(models.Model):
	name = models.CharField(max_length=30)
	rating = models.FloatField(default=2 )
	rater_count = models.IntegerField(default=0)
	rated_overall = models.IntegerField(default=0)


class  Room(models.Model):
	room_type = models.CharField(max_length=15, choices=ROOM_CHOICES)
	room_count = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
	hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)