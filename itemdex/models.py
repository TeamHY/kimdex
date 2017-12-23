from django.db import models

class Item(models.Model):
	game_id		= models.IntegerField(default = 0)
	category	= models.IntegerField(default = 0)
	name		= models.CharField(max_length = 20)
	text		= models.CharField(max_length = 500)

	def __str__(self):
		return self.name
