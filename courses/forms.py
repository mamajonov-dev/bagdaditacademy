from django import forms
from .models import *


class CourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Course
        fields = ('name',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'course', 'room', 'teacher', 'amount', 'continuity', 'room_time']

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )
