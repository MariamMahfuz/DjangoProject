from django.db import models
from froala_editor.fields import FroalaField



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


# class Upcoming(models.Model):
#     heading = models.CharField(max_length=80)
#     amount = models.IntegerField(blank=True, null=True)
#     image = models.ImageField(upload_to='card')
#     heading_tag = models.CharField(max_length=80)
#     description = models.CharField(max_length=300)
#     date=models.DateField(null=True)


class Heading(models.Model):
    title = models.CharField(blank=True, max_length=80)
    meeting_detail_heading = models.CharField(blank=True, max_length=50)


class Up_Events(models.Model):
    title = models.CharField(blank=True, max_length=80)
    amount = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='card')
    description = models.CharField(max_length=300)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title


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


class metting_details(models.Model):
    title = models.ForeignKey(Up_Events, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    descriptions = models.TextField(max_length=2000)
    hours = models.CharField(max_length=400)
    booking_number = models.CharField(blank=True, max_length=30)
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    behance = models.URLField(max_length=100)

    def __str__(self):
        return str(self.title)


class EmployeeForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    # state = models.CharField(max_length=20)
    zip = models.IntegerField(max_length=30)
    website = models.URLField(max_length=200)
    hosting = models.CharField(max_length=10)
    comment = models.CharField(max_length=300)

class StateName(models.Model):
    state=models.CharField(max_length=20)
    def __str__(self):
        return str(self.title)





