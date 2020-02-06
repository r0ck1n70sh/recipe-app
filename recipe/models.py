from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Ingredient(models.Model):
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def __unicode__self(self):
		return self.name

class Post(models.Model):
	title= models.CharField(max_length=100)

	author= models.ForeignKey(User, on_delete=models.CASCADE)

	description= models.TextField()

	post_pic= models.ImageField(default='recipe_pics/default.jpg', upload_to='recipe_pics')

	date_posted= models.DateTimeField(default=timezone.now)

	used_ingredients=models.ManyToManyField(Ingredient)

	steps= models.TextField()

	def __str__(self):
		return self.title

	def __unicode__self(self):
		return self.title

	def get_absolute_url(self):
		return reverse('recipe-detail', kwargs={'pk':self.pk})

	def save(self):
		super().save()
		img= Image.open(self.post_pic.path)

		if img.height > 1024 or img.width > 768:
			output_size= (1024, 768)
			img.thumbnail(output_size)
			img.save(self.post_pic.path)
