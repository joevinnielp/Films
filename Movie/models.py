from django.db import models

# Create your models here.

class Film(models.Model):
	Title = models.CharField(max_length=150)
	Description = models.TextField()
	Year = models.DateTimeField('Date Published')

	actor = models.ManyToManyField ("Actor", related_name="Film")
	genre = models.ManyToManyField ("Genre", related_name="Film")

	def __str__(self):
		return "{} by {} - {}".format(self.Title, self.list_actor(), self.list_genre())

	def list_actor(self):
		return ",".join([actor.Actor_name for actor in self.actor.all()])

	def list_genre(self):
		return ",".join([genre.Type for genre in self.genre.all()])

	def save(self, *args, **kwargs):
		super(Film, self).save(*args, **kwargs)

class Actor(models.Model):
	Actor_name = models.CharField(max_length=150)

	def __str__(self):
		return self.Actor_name

class Genre(models.Model):
	Type = models.CharField(max_length=150)

	def __str__(self):
		return self.Type