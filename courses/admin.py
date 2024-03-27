from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Course)

admin.site.register(Room)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'complete', 'start', 'finish']