import datetime

from django.db import models
from uuid import uuid4
from teachers.models import Teacher
from dateutil.relativedelta import relativedelta



class Room(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    CHOICES = (
        ('8-00', '10-00'),
        ('9-00', '11-00'),
        ('10-00', '12-00'),
        ('11-00', '13-00'),
        ('12-00', '14-00'),
        ('13-00', '15-00'),
        ('14-00', '16-00'),
        ('15-00', '17-00'),
        ('16-00', '18-00'),
    )
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True, default=200000)
    complete = models.BooleanField(default=False, blank=True, null=True)
    continuity = models.IntegerField(default=1, blank=True, null=True)
    start = models.DateField(blank=True, null=True, auto_created=True)

    finish = models.DateField(blank=True, null=True, auto_created=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, blank=True, null=True)
    room_time = models.CharField(max_length=200, choices=CHOICES, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return self.name
    def len_students(self):
        student = self.student_set.all()
        return len(student)

    def amount_payment(self):
        amount = self.len_students() * self.amount * self.continuity
        return amount

    def group_prosses(self):
        # now = datetime.date.today()
        # start = self.start
        # finish = self.finish
        # # pount =  float(str((100 / float(str((finish - start)).split()[0]) )).split()[0]) * float(str((now - start)).split()[0])
        # y, m, d = map(int, str(self.start).split('-'))
        # start = datetime.date(y, m, d)
        # finish = relativedelta(months=self.continuity) - datetime.date(y, m, d)
        now = datetime.date.today().month
        hozirgacha = self.start - relativedelta(months=now)

        return hozirgacha