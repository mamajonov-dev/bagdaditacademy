from django.urls import path
from .views import *

urlpatterns = [
    path('', all_teachers, name='all_teachers'),
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('teacher-profile/<str:pk>/', teacher_profile, name='teacher_profile'),
]