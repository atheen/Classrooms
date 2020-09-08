from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField(default=1)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
	FEMALE = 'F'
	MALE = 'M'
	GENDER_CHOICES = [
		(FEMALE,'Female'),
		(MALE,'Male')
	]
	name = models.CharField(max_length=120)
	dob = models.DateField()
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=FEMALE)
	exam_grade = models.FloatField(blank=True)
	classroom = models.ForeignKey(Classroom, default=1, on_delete=models.CASCADE)


	def __str__(self):
		return self.name
