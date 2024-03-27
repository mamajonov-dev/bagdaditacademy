from django.urls import path
from .views import *

urlpatterns = [
    path('', groups_view, name='all_groups'),
    path('all-courses/', courses_view, name='all_courses'),
    path('delete-course/<str:pk>/', delete_course, name='delete_course'),
    path('delete-group/<str:pk>/', delete_group, name='delete_group'),
    path('add-course/', add_course, name='add_course'),
    path('add-group/', add_group, name='add_group'),
    path('group/<str:pk>/', group_detail, name='group_detail'),
    path('complete-group/<str:pk>/', complate_group, name='complate_group'),
    path('add-student-to-group/<str:group_id>/<str:student_id>/', add_student_to_group, name='add_student_to_group'),
    # path('start-group/<str:pk>/', start_group, name='start_group'),
]