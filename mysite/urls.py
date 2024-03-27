from django.urls import path
from .views import *
urlpatterns = [
    path('', my_site, name='my_site'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='logout'),
    path('login/', login_user, name='login'),
]