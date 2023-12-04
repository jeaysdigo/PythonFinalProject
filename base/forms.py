from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lesson, User



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

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'



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

