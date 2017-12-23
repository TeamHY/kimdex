from django.db import models

class Item(models.Model):
	game_id		= models.IntegerField(default = 0)
	item_type	= models.IntegerField(default = 0)
	item_text	= models.CharField(max_length = 500)

	def __str__(self):
		return self.item_text