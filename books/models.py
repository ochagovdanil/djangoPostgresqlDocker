from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	year = models.IntegerField(validators=[
		MinValueValidator(0),
		MaxValueValidator(3000),
	])
