from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lesson, User, Unit



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            # 'bio',
            # 'courses',
            'email',
            'password1',
            'password2',
        ]

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

# class LessonForm(ModelForm):
#     class Meta:
#         model = Lesson
#         fields = '__all__'
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'units']

    # Add this if you want to customize the units field widget
    units = forms.ModelMultipleChoiceField(
        queryset=Unit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['title', 'number', 'course']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
            'first_name', 
            'last_name', 
            'email', 
            'bio', 

            'username',
            ]

