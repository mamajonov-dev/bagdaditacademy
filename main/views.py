from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teachers.models import *
from students.models import *
from courses.models import *

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_staff:

        teachers = Teacher.objects.all()
        students = Student.objects.all()
        groups = Group.objects.all()
        rooms = Room.objects.all()
        course = Course.objects.all()
        payment = Payment.objects.all()

        context = {
            'teachers': len(teachers),
            'students':len(students),
            'groups': len(groups),
            'rooms': len(rooms),
            'course': len(course),
            'payment': len(payment)
        }
        return render(request, 'index.html', context)
    else:
        return redirect('my_site')


# def register_student(request):
#     students = Student.objects.filter(group=None)
#     context = {
#         'students': students,
#     }
#     return render(request, 'registartions.html', context)

# def blank(request):
#     return render(request, 'starter-kit.html')
# def profile(request):
#     return render(request, 'pages-profile.html')
# def form_v(request):
#     return render(request, 'form-basic.html')
# def icons(request):
#     return render(request, 'icon-material.html')
