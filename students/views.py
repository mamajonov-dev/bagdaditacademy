from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import io
import qrcode


from .models import *
from .forms import *

#
def students(request):
    students = Student.objects.all().order_by('full_name')
    context = {
        'students': students,
    }
    return render(request, 'students-table.html', context)

def add_student(request):
    form = SudentForm()
    if request.method == 'POST':
        form = SudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('students')
    context = {
        'form': form
    }
    return render(request, 'add-student.html', context)


def student_profile(request, pk):
    student = Student.objects.get(id=pk)
    groups = student.group
    context = {
        'student': student,
        'groups': groups
    }
    return render(request, 'student-profile.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':

        payments = Payment.objects.filter(student=student)
        for payment in payments:
            payment.delete()

        student.delete()
        return redirect('students')
    context = {
        'item': student.full_name,
        'orqaga': 'students'
    }
    return render(request, 'delete-item.html', context)

def payments(request):
    payment = Payment.objects.filter(complate=False)
    context = {
        'payments': payment,
    }
    return render(request, 'payments-table.html', context)

def pay_for_student(request, pk):
    payment = Payment.objects.get(id=pk)
    form = PaymentForm(instance=payment)
    if request.method == 'POST':
        form = PaymentForm(instance=payment, data=request.POST, files=request.FILES)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.month = payment.month
            pay.student = payment.student
            pay.to_group = payment.to_group
            pay.complate = True

            pay.save()

            return redirect('payments')
    context = {
        'form': form,
        'student': payment.student,
        'month': payment.month
    }
    return render(request, 'pay_for_student-form.html', context)


def generate_certificate(request, pk):

    student = Student.objects.get(id=pk)
    course = student.course
    try:
        student = Studentcertificate.objects.get(student=student, course=course)
        return redirect('students')
    except:
        student_name = student.full_name.split()
        if len(student_name) > 1:
            student_name = f"{student_name[0]} {student_name[1]}"
        else:
            student_name = f"{student_name[0]}"
        img = Image.open('static/certificate.png')
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("Roboto-Regular.ttf", 210)
        d.text((150,1000), f"{student_name}", fill=(0,0,0), font=font)


        # Сохраняем изображение в объект BytesIO
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        # Предположим, что buffer - это объект StringIO, содержащий PNG-данные
        # Создаем объект PIL Image из данных StringIO
        img1 = Image.open(buffer)

        # Сохраняем изображение в файл
        img1.save(f"static/certificates/{student_name}{student.id}.png", format="PNG")

        Studentcertificate.objects.create(
            student=student,
            image=f"static/certificates/{student.full_name}{student.id}.png",
            course=student.course
        )

        # Отправляем изображение в ответе
        return HttpResponse(buffer.getvalue(), content_type="image/png", content={"students": Student.objects.all(),})
    #
    # return render(request,'students-table.html', context=)