from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from datetime import date
from .models import Student, Attendance, MessBill
from .forms import StudentForm


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'accounts/add_student.html', {'form': form})


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'accounts/student_list.html', {'students': students})


@login_required
def mark_attendance(request):
    students = Student.objects.all()
    today = date.today()

    if request.method == "POST":
        for student in students:
            status = request.POST.get(str(student.id))
            is_present = True if status == "on" else False

            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={'is_present': is_present}
            )

        return redirect('student_list')

    return render(request, 'accounts/mark_attendance.html', {
        'students': students,
        'today': today
    })


@login_required
def generate_bill(request):
    today = date.today()
    students = Student.objects.all()
    cost_per_day = 100

    for student in students:
        present_days = Attendance.objects.filter(
            student=student,
            date__month=today.month,
            date__year=today.year,
            is_present=True
        ).count()

        total_days = Attendance.objects.filter(
            student=student,
            date__month=today.month,
            date__year=today.year
        ).count()

        amount = present_days * cost_per_day

        MessBill.objects.update_or_create(
            student=student,
            month=today.month,
            year=today.year,
            defaults={
                'total_days': total_days,
                'present_days': present_days,
                'amount': amount
            }
        )

    return redirect('student_list')


@login_required
def bill_list(request):
    bills = MessBill.objects.all()
    return render(request, 'accounts/bill_list.html', {'bills': bills})


def logout_view(request):
    logout(request)
    return redirect('login')