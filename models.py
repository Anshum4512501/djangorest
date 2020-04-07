from django.db import models

# Create your models here.

class Paradigm(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self):
        return self.name



class Languages(models.Model):
    name = models.CharField(max_length= 100)
    paradigm = models.ForeignKey(Paradigm,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length= 100)
    languages = models.ManyToManyField(Languages)
    def __str__(self):
        return self.name


class Activity(models.Model):
    start_time = models.CharField(max_length=100)
    end_time_time = models.CharField(max_length=100)
    def __str__(self):
        return "activity start time = "+self.start_time

     
class Manager(models.Model):
    id = models.CharField(primary_key=True,max_length = 100)
    real_name = models.CharField(max_length=100)
    tz=models.CharField(max_length=50)
    activity = models.ManyToManyField(Activity)
    def __str__(self):
        return self.real_name

class Throttle(models.Model):
    ok = models.BooleanField(default=True)
    manager = models.ManyToManyField(Manager)
 
    def __str__(self):
        return self.name
  