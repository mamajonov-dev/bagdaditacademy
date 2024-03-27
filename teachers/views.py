from django.shortcuts import render, redirect
from .models import *
from students.models import Student, Group


def all_teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }

    return render(request, 'teachers-table.html', context)

def teacher_profile(request, pk):
    teacher = Teacher.objects.get(id=pk)
    groups = teacher.group_set.all()
    # students = groups.student_set.all()
    context = {
        'teacher': teacher,
        'groups': groups,
        # 'students': students
    }
    return render(request, 'teacher-profile.html', context)


def add_teacher(request):

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        Teacher.objects.create(
            user=request.user,
            name=full_name
        )
        return redirect('all_teachers')


    return render(request, 'add-teacher.html')

