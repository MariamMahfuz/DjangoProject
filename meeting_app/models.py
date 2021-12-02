from django.db import models


# Create your models here.
class Cover(models.Model):
    image = models.ImageField(upload_to='cover')
    address = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)


class Service(models.Model):
    icon = models.ImageField(upload_to='card')
    heading = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)


class Upcoming(models.Model):
    heading = models.CharField(max_length=80)
    amount = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='card')
    # date=models.DateField()
    heading_tag = models.CharField(max_length=80)
    description = models.CharField(max_length=300)


class Courses(models.Model):
    heading = models.CharField(max_length=30)
    image = models.ImageField(upload_to='card')
    description = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)


class Overview(models.Model):
    head = models.CharField(max_length=200)
    Success_percent = models.IntegerField(blank=True, null=True)
    Succesed = models.CharField(max_length=30)
    Member_Number = models.IntegerField(blank=True, null=True)
    Member = models.CharField(max_length=30)
    Mentor_number = models.IntegerField(blank=True, null=True)
    Mentor = models.CharField(max_length=30)
    Award_number = models.IntegerField(blank=True, null=True)
