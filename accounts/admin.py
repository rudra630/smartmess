from django.contrib import admin
from .models import Student
from .models import Attendance,MessBill


admin.site.register(Student)

admin.site.register(Attendance)
admin.site.register(MessBill)
