from django.urls import path
from .views import *

urlpatterns = [

    path('students/', students, name='students'),
    path('student-profile/<str:pk>/', student_profile, name='student_profile'),
    path('delete-student/<str:pk>/', delete_student, name='delete_student'),

    path('getimage/<str:pk>/', generate_certificate, name='getimage'),
    path('payments/', payments, name='payments'),
    path('add-student/', add_student, name='add_student'),
    path('pay-for-student/<str:pk>/', pay_for_student, name='pay_for_student'),

]