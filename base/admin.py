from django.contrib import admin

# Register your models here.

from .models import Course, Lesson, Question, Quiz, QuizAttempt, User
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizAttempt)
