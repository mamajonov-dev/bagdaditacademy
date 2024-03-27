from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['month', 'student', 'amount', 'complate']
    ordering = ['month']
    list_filter = ['amount', 'month']

@admin.register(Studentcertificate)
class StudentcertificateAdmin(admin.ModelAdmin):
    list_display = ['student', 'image']
    ordering = ['student']


