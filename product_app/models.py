from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	weight = models.FloatField()
	price = models.FloatField()
	class Meta:
		db_table="Product"
	def __str__(self):
		return self.name