from django.db import models
from courses.models import Group, Course
from uuid import uuid4


class Student(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=9, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    finish = models.BooleanField(default=False, blank=True, null=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name

    def len_not_amount(self):
        if self.group:
            amount = self.payment_set.filter(complate=False)
            return len(amount)

    def sertificate(self):
        if self.group:
            amount = self.payment_set.filter(complate=False)
            group_continuity = self.group.continuity
            if len(amount) == 0:
                count = True
            else:
                count = False
            return count

class Payment(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=200, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    to_group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    sale = models.IntegerField(default=0, blank=True, null=True)
    payment_check = models.ImageField(upload_to='payment_cheks/', blank=True, null=True, default=None)
    complate = models.BooleanField(default=False, blank=True, null=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.month

    # class Meta:
    #     ordering = ('int(month)', )




class Studentcertificate(models.Model):
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.student.full_name