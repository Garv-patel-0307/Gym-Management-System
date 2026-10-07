from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True, max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    joined_date = models.DateField()
    img = models.ImageField()

class Biceps(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Triceps(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Forearms(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Leg(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Back(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Chest(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Shoulder(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)

class Abs(models.Model):
    username = models.CharField(max_length=30)
    exercise = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=15)
    set_1 = models.CharField(max_length=20, default=0)
    set_2 = models.CharField(max_length=20, default=0)
