from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('register_student/', register_student, name='register_student'),
    #
    #
    #
    # path('forms_v', form_v, name='forms_v'),
    # path('icons/', icons, name='icons'),
    # path('blank/', blank, name='blank'),
    # path('profile/', profile, name='profile'),
]