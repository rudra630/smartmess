from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('generate-bill/', views.generate_bill, name='generate_bill'),
    path('bills/', views.bill_list, name='bill_list'),
    path('logout/', views.logout_view, name='logout'),
]