from django.db import models
from django.utils import timezone


#Define the model for the Customer table
class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    nu_id = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__ (self):
        return self.student_name

class Club(models.Model):
    club_name = models.CharField(max_length=100)
    club_category = models.CharField(max_length=100)
    club_description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.club_name)

class Event(models.Model):
    Club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='clubs')
    event_name = models.CharField(max_length=50)
    event_category = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.event_name)

class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
    meal_description = models.CharField(max_length=200)
    meal_drink = models.CharField(max_length=200)
    price = models.CharField(max_length=200)







