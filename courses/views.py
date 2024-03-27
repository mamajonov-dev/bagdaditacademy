from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime
from dateutil.relativedelta import relativedelta
from .models import Course, Group, Room
from students.models import Student, Payment
from .forms import *


def courses_view(request):
    all_courses = Course.objects.all()
    context = {
        'courses': all_courses
    }
    return render(request, 'courses-table.html', context)


def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('all_courses')
    context = {
        'item': course.name,
        'orqaga': 'courses'
    }
    return render(request, 'delete-item.html', context)


def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('all_courses')

    context = {
        'form': form
    }
    return render(request, 'add-course.html', context)


def groups_view(request):
    all_groups = Group.objects.all().order_by('-created')
    context = {
        'groups': all_groups
    }
    return render(request, 'groups-table.html', context)


def add_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('all_groups')
    context = {
        'form': form
    }
    return render(request, 'add-group.html', context)


def group_detail(request, pk):
    group = Group.objects.get(id=pk)
    if not group.start:
        if request.method == 'POST':
            start_date = request.POST.get('start-group')
            if start_date and group.continuity != 0:
                y, m, d = map(int, str(start_date).split('-'))
                group.start = datetime.date(y, m, d)
                group.finish = datetime.date(y, m, d) + relativedelta(months=group.continuity)
                group.save()
            elif group.continuity == 0:
                y, m, d = map(int, str(start_date).split('-'))
                group.start = datetime.date(y, m, d)
                group.finish = group.start
                group.save()

    students = Student.objects.filter(group=group)
    new_students = Student.objects.filter(course=group.course, group=None)
    payments = Payment.objects.filter(complate=False, to_group=group)

    payments_list = list()
    for i in range(1, group.continuity + 1):
        month = []
        for payment in payments:
            if payment.month == str(i):
                month.append(payment)
        if len(students) != 0:
            pount = 100 / len(students) * (len(students) - len(month))
            payments_list.append((i, month, pount))

    context = {
        "group": group,
        "students": students,
        "new_students": new_students,
        'payments_list': payments_list,
        'count': range(1, group.continuity + 1)

    }
    return render(request, 'group_detail.html', context)


def add_student_to_group(request, group_id, student_id, ):
    group = Group.objects.get(id=group_id)
    student = Student.objects.get(id=student_id)

    student.group = group
    student.save()
    for i in range(1, group.continuity + 1):
        Payment.objects.create(
            amount=group.amount,
            month=i,
            student=student,
            to_group=group,
            note='',
            complate=False
        )

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':

        payments = Payment.objects.filter(to_group=group, complate=False)
        for payment in payments:
            payment.delete()
        group.delete()
        return redirect('all_groups')
    context = {
        'item': group.name,
        'orqaga': 'groups'
    }
    return render(request, 'delete-item.html', context)


def complate_group(request, pk):

    group = Group.objects.get(id=pk)


    group.complete = True
    group.save()
    return redirect('group_detail', pk=group.id)

    # return render(request, 'group_detail.html')
