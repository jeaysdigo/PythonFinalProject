from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import Choice, Course, Lesson, Question, Quiz, User, Unit



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

from django import forms
from .models import Quiz, Question

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)

        # Customize the checkboxes using Tailwind CSS classes
        self.fields['questions'].widget.attrs.update({
            'class': 'grid gap-2 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 border',  # Flexbox classes for inline display and border
        })

        # Add individual Tailwind CSS classes for each checkbox
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-checkbox'  # Adjust spacing and other styles
            else:
                field.widget.attrs['class'] = 'form-checkbox'

        # You can add more Tailwind CSS classes or customize as needed

    
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
        widgets = {
            'is_correct': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-green-600 bg-gray-100 border-gray-300 rounded focus:ring-[#25A76F]'}),
            'text': forms.TextInput(attrs={'class': 
                                           'w-full border border-gray-300 ml-4 rounded-lg p-2 focus:outline-green-600 ',
                                           'placeholder':'Enter Choice'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        

ChoiceFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=4)
ChoiceFormEdit = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=0)


