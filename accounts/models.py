from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    room_no = models.CharField(max_length=10)
    mess_fee = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.name} - {self.date}"
class MessBill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    total_days = models.IntegerField()
    present_days = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.month}/{self.year}"
